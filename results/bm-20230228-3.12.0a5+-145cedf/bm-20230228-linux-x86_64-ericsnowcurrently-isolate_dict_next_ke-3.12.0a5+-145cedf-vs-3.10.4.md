
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_dict_next_ke
- machine: linux-x86_64
- commit hash: 145cedf
- commit date: 2023-02-28
- overall geometric mean: 1.28x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                              |
| chameleon      | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                             |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                            |
| html5lib       | 85.9 ms                                                | 62.5 ms: 1.37x faster                                                             |
| tornado_http   | 128 ms                                                 | 95.2 ms: 1.35x faster                                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.6 ms: 1.54x faster                                                             |
| float          | 109 ms                                                 | 75.1 ms: 1.45x faster                                                             |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                             |
| regex_dna      | 214 ms                                                 | 200 ms: 1.07x faster                                                              |
| regex_effbot   | 3.19 ms                                                | 3.62 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 290 us: 1.56x faster                                                              |
| unpickle_pure_python | 302 us                                                 | 203 us: 1.48x faster                                                              |
| json_dumps           | 13.4 ms                                                | 9.59 ms: 1.40x faster                                                             |
| xml_etree_process    | 74.5 ms                                                | 56.0 ms: 1.33x faster                                                             |
| json_loads           | 28.7 us                                                | 24.2 us: 1.18x faster                                                             |
| xml_etree_generate   | 93.8 ms                                                | 81.8 ms: 1.15x faster                                                             |
| pickle_list          | 4.72 us                                                | 4.22 us: 1.12x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.10x faster                                                              |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| unpickle             | 14.2 us                                                | 13.8 us: 1.02x faster                                                             |
| unpickle_list        | 4.92 us                                                | 5.29 us: 1.07x slower                                                             |
| pickle_dict          | 27.6 us                                                | 31.5 us: 1.14x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                      |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.07 ms: 1.55x faster                                                             |
| python_startup_no_site | 5.78 ms                                                | 6.57 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                             |
| genshi_text     | 30.6 ms                                                | 21.6 ms: 1.42x faster                                                             |
| django_template | 46.3 ms                                                | 33.8 ms: 1.37x faster                                                             |
| genshi_xml      | 63.7 ms                                                | 48.0 ms: 1.33x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.8 ms: 2.48x faster                                                             |
| deltablue               | 7.28 ms                                                | 3.25 ms: 2.24x faster                                                             |
| logging_silent          | 176 ns                                                 | 96.0 ns: 1.84x faster                                                             |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                                              |
| asyncio_tcp             | 914 ms                                                 | 500 ms: 1.83x faster                                                              |
| richards                | 75.2 ms                                                | 44.2 ms: 1.70x faster                                                             |
| go                      | 226 ms                                                 | 139 ms: 1.63x faster                                                              |
| raytrace                | 467 ms                                                 | 295 ms: 1.58x faster                                                              |
| crypto_pyaes            | 117 ms                                                 | 73.8 ms: 1.58x faster                                                             |
| spectral_norm           | 150 ms                                                 | 94.8 ms: 1.58x faster                                                             |
| pyflate                 | 676 ms                                                 | 429 ms: 1.58x faster                                                              |
| chaos                   | 106 ms                                                 | 67.1 ms: 1.57x faster                                                             |
| pickle_pure_python      | 452 us                                                 | 290 us: 1.56x faster                                                              |
| python_startup          | 14.1 ms                                                | 9.07 ms: 1.55x faster                                                             |
| nbody                   | 144 ms                                                 | 93.6 ms: 1.54x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                 | 70.7 ms: 1.53x faster                                                             |
| hexiom                  | 9.43 ms                                                | 6.16 ms: 1.53x faster                                                             |
| unpickle_pure_python    | 302 us                                                 | 203 us: 1.48x faster                                                              |
| deepcopy_memo           | 51.7 us                                                | 35.0 us: 1.48x faster                                                             |
| mako                    | 14.7 ms                                                | 10.0 ms: 1.46x faster                                                             |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                              |
| float                   | 109 ms                                                 | 75.1 ms: 1.45x faster                                                             |
| chameleon               | 9.17 ms                                                | 6.42 ms: 1.43x faster                                                             |
| genshi_text             | 30.6 ms                                                | 21.6 ms: 1.42x faster                                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                             |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.40x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.59 ms: 1.40x faster                                                             |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.40x faster                                                             |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 685 ms: 1.39x faster                                                              |
| logging_format          | 8.85 us                                                | 6.39 us: 1.39x faster                                                             |
| logging_simple          | 8.10 us                                                | 5.86 us: 1.38x faster                                                             |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                            |
| html5lib                | 85.9 ms                                                | 62.5 ms: 1.37x faster                                                             |
| django_template         | 46.3 ms                                                | 33.8 ms: 1.37x faster                                                             |
| unpack_sequence         | 59.4 ns                                                | 43.6 ns: 1.36x faster                                                             |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                              |
| coroutines              | 31.6 ms                                                | 23.4 ms: 1.35x faster                                                             |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                              |
| fannkuch                | 488 ms                                                 | 362 ms: 1.35x faster                                                              |
| tornado_http            | 128 ms                                                 | 95.2 ms: 1.35x faster                                                             |
| thrift                  | 1.03 ms                                                | 770 us: 1.34x faster                                                              |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                              |
| xml_etree_process       | 74.5 ms                                                | 56.0 ms: 1.33x faster                                                             |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                             |
| genshi_xml              | 63.7 ms                                                | 48.0 ms: 1.33x faster                                                             |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| async_tree_memoization  | 855 ms                                                 | 650 ms: 1.32x faster                                                              |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                             |
| deepcopy                | 438 us                                                 | 337 us: 1.30x faster                                                              |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                              |
| mypy2                   | 430 ms                                                 | 334 ms: 1.29x faster                                                              |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 749 ms: 1.27x faster                                                              |
| deepcopy_reduce         | 3.79 us                                                | 3.00 us: 1.26x faster                                                             |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.40 ms: 1.24x faster                                                             |
| nqueens                 | 100 ms                                                 | 81.8 ms: 1.22x faster                                                             |
| dulwich_log             | 75.8 ms                                                | 63.1 ms: 1.20x faster                                                             |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                              |
| bench_thread_pool       | 946 us                                                 | 799 us: 1.18x faster                                                              |
| json_loads              | 28.7 us                                                | 24.2 us: 1.18x faster                                                             |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                                             |
| sympy_integrate         | 24.0 ms                                                | 20.7 ms: 1.16x faster                                                             |
| sympy_expand            | 534 ms                                                 | 462 ms: 1.15x faster                                                              |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                             |
| xml_etree_generate      | 93.8 ms                                                | 81.8 ms: 1.15x faster                                                             |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                             |
| sympy_str               | 325 ms                                                 | 287 ms: 1.13x faster                                                              |
| pickle_list             | 4.72 us                                                | 4.22 us: 1.12x faster                                                             |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.10x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                                             |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                              |
| sympy_sum               | 183 ms                                                 | 169 ms: 1.09x faster                                                              |
| regex_dna               | 214 ms                                                 | 200 ms: 1.07x faster                                                              |
| telco                   | 6.73 ms                                                | 6.36 ms: 1.06x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.65 sec: 1.04x faster                                                            |
| unpickle                | 14.2 us                                                | 13.8 us: 1.02x faster                                                             |
| async_generators        | 426 ms                                                 | 423 ms: 1.01x faster                                                              |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                              |
| unpickle_list           | 4.92 us                                                | 5.29 us: 1.07x slower                                                             |
| gc_traversal            | 3.53 ms                                                | 3.84 ms: 1.09x slower                                                             |
| regex_effbot            | 3.19 ms                                                | 3.62 ms: 1.13x slower                                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.57 ms: 1.14x slower                                                             |
| pickle_dict             | 27.6 us                                                | 31.5 us: 1.14x slower                                                             |
| dask                    | 436 ms                                                 | 509 ms: 1.17x slower                                                              |
| coverage                | 74.7 ms                                                | 95.0 ms: 1.27x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                                      |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-145cedf/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf.json: comprehensions
