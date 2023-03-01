
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: 969caba
- commit date: 2023-02-28
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                                              |
| chameleon      | 9.17 ms                                                | 6.33 ms: 1.45x faster                                                             |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                            |
| html5lib       | 85.9 ms                                                | 61.9 ms: 1.39x faster                                                             |
| tornado_http   | 128 ms                                                 | 95.3 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.6 ms: 1.54x faster                                                             |
| float          | 109 ms                                                 | 73.8 ms: 1.48x faster                                                             |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                             |
| regex_dna      | 214 ms                                                 | 200 ms: 1.07x faster                                                              |
| regex_effbot   | 3.19 ms                                                | 3.55 ms: 1.11x slower                                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 285 us: 1.59x faster                                                              |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                              |
| json_dumps           | 13.4 ms                                                | 9.61 ms: 1.40x faster                                                             |
| xml_etree_process    | 74.5 ms                                                | 55.6 ms: 1.34x faster                                                             |
| json_loads           | 28.7 us                                                | 23.8 us: 1.20x faster                                                             |
| pickle_list          | 4.72 us                                                | 4.01 us: 1.18x faster                                                             |
| xml_etree_generate   | 93.8 ms                                                | 80.7 ms: 1.16x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 99.1 ms: 1.12x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                                             |
| pickle               | 10.2 us                                                | 9.95 us: 1.02x faster                                                             |
| pickle_dict          | 27.6 us                                                | 29.7 us: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.03 ms: 1.56x faster                                                             |
| python_startup_no_site | 5.78 ms                                                | 6.55 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.2 ms: 1.44x faster                                                             |
| genshi_text     | 30.6 ms                                                | 21.5 ms: 1.42x faster                                                             |
| django_template | 46.3 ms                                                | 33.2 ms: 1.40x faster                                                             |
| genshi_xml      | 63.7 ms                                                | 48.2 ms: 1.32x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.7 ms: 2.49x faster                                                             |
| deltablue               | 7.28 ms                                                | 3.19 ms: 2.28x faster                                                             |
| logging_silent          | 176 ns                                                 | 92.6 ns: 1.91x faster                                                             |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                              |
| asyncio_tcp             | 914 ms                                                 | 498 ms: 1.83x faster                                                              |
| richards                | 75.2 ms                                                | 42.2 ms: 1.78x faster                                                             |
| go                      | 226 ms                                                 | 133 ms: 1.69x faster                                                              |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                                              |
| raytrace                | 467 ms                                                 | 285 ms: 1.64x faster                                                              |
| scimark_monte_carlo     | 109 ms                                                 | 66.7 ms: 1.63x faster                                                             |
| chaos                   | 106 ms                                                 | 66.3 ms: 1.59x faster                                                             |
| pickle_pure_python      | 452 us                                                 | 285 us: 1.59x faster                                                              |
| spectral_norm           | 150 ms                                                 | 95.8 ms: 1.56x faster                                                             |
| python_startup          | 14.1 ms                                                | 9.03 ms: 1.56x faster                                                             |
| crypto_pyaes            | 117 ms                                                 | 75.1 ms: 1.55x faster                                                             |
| hexiom                  | 9.43 ms                                                | 6.11 ms: 1.54x faster                                                             |
| nbody                   | 144 ms                                                 | 93.6 ms: 1.54x faster                                                             |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                              |
| deepcopy_memo           | 51.7 us                                                | 34.1 us: 1.52x faster                                                             |
| float                   | 109 ms                                                 | 73.8 ms: 1.48x faster                                                             |
| chameleon               | 9.17 ms                                                | 6.33 ms: 1.45x faster                                                             |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.44x faster                                                              |
| mako                    | 14.7 ms                                                | 10.2 ms: 1.44x faster                                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                             |
| genshi_text             | 30.6 ms                                                | 21.5 ms: 1.42x faster                                                             |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                                            |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.40x faster                                                             |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.61 ms: 1.40x faster                                                             |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.40x faster                                                             |
| pprint_safe_repr        | 953 ms                                                 | 687 ms: 1.39x faster                                                              |
| html5lib                | 85.9 ms                                                | 61.9 ms: 1.39x faster                                                             |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                            |
| logging_format          | 8.85 us                                                | 6.41 us: 1.38x faster                                                             |
| logging_simple          | 8.10 us                                                | 5.87 us: 1.38x faster                                                             |
| async_tree_none         | 711 ms                                                 | 519 ms: 1.37x faster                                                              |
| coroutines              | 31.6 ms                                                | 23.1 ms: 1.37x faster                                                             |
| async_tree_memoization  | 855 ms                                                 | 632 ms: 1.35x faster                                                              |
| tornado_http            | 128 ms                                                 | 95.3 ms: 1.34x faster                                                             |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                                              |
| unpack_sequence         | 59.4 ns                                                | 44.3 ns: 1.34x faster                                                             |
| xml_etree_process       | 74.5 ms                                                | 55.6 ms: 1.34x faster                                                             |
| thrift                  | 1.03 ms                                                | 775 us: 1.33x faster                                                              |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                              |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                              |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                             |
| scimark_fft             | 421 ms                                                 | 318 ms: 1.32x faster                                                              |
| genshi_xml              | 63.7 ms                                                | 48.2 ms: 1.32x faster                                                             |
| fannkuch                | 488 ms                                                 | 370 ms: 1.32x faster                                                              |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                             |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.31x faster                                                              |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                                             |
| mypy2                   | 430 ms                                                 | 334 ms: 1.29x faster                                                              |
| deepcopy_reduce         | 3.79 us                                                | 2.94 us: 1.29x faster                                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 737 ms: 1.29x faster                                                              |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                            |
| nqueens                 | 100 ms                                                 | 82.8 ms: 1.21x faster                                                             |
| json_loads              | 28.7 us                                                | 23.8 us: 1.20x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                                              |
| bench_thread_pool       | 946 us                                                 | 796 us: 1.19x faster                                                              |
| dulwich_log             | 75.8 ms                                                | 64.2 ms: 1.18x faster                                                             |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.2 ms: 1.18x faster                                                             |
| pickle_list             | 4.72 us                                                | 4.01 us: 1.18x faster                                                             |
| json                    | 5.35 ms                                                | 4.59 ms: 1.16x faster                                                             |
| sympy_integrate         | 24.0 ms                                                | 20.7 ms: 1.16x faster                                                             |
| xml_etree_generate      | 93.8 ms                                                | 80.7 ms: 1.16x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.73 ms: 1.15x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.38 sec: 1.15x faster                                                            |
| sympy_expand            | 534 ms                                                 | 464 ms: 1.15x faster                                                              |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                             |
| sympy_str               | 325 ms                                                 | 287 ms: 1.13x faster                                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                             |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                             |
| djangocms               | 36.9 us                                                | 32.9 us: 1.12x faster                                                             |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 99.1 ms: 1.12x faster                                                             |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| sympy_sum               | 183 ms                                                 | 169 ms: 1.09x faster                                                              |
| regex_dna               | 214 ms                                                 | 200 ms: 1.07x faster                                                              |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                                             |
| telco                   | 6.73 ms                                                | 6.48 ms: 1.04x faster                                                             |
| async_generators        | 426 ms                                                 | 418 ms: 1.02x faster                                                              |
| pickle                  | 10.2 us                                                | 9.95 us: 1.02x faster                                                             |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| pickle_dict             | 27.6 us                                                | 29.7 us: 1.08x slower                                                             |
| gc_traversal            | 3.53 ms                                                | 3.83 ms: 1.09x slower                                                             |
| regex_effbot            | 3.19 ms                                                | 3.55 ms: 1.11x slower                                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.55 ms: 1.13x slower                                                             |
| dask                    | 436 ms                                                 | 506 ms: 1.16x slower                                                              |
| coverage                | 74.7 ms                                                | 93.7 ms: 1.25x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                      |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-969caba/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba.json: comprehensions
