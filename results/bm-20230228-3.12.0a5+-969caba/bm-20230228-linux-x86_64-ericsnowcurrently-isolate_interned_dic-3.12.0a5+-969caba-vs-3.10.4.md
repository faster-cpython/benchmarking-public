
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: 969caba
- commit date: 2023-02-28
- overall geometric mean: 1.28x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                              |
| chameleon      | 9.17 ms                                                | 6.44 ms: 1.42x faster                                                             |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                            |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.39x faster                                                             |
| tornado_http   | 128 ms                                                 | 95.3 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.4 ms: 1.56x faster                                                             |
| float          | 109 ms                                                 | 73.4 ms: 1.48x faster                                                             |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                             |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                                              |
| regex_effbot   | 3.19 ms                                                | 3.67 ms: 1.15x slower                                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 293 us: 1.54x faster                                                              |
| unpickle_pure_python | 302 us                                                 | 203 us: 1.49x faster                                                              |
| json_dumps           | 13.4 ms                                                | 9.47 ms: 1.42x faster                                                             |
| xml_etree_process    | 74.5 ms                                                | 56.1 ms: 1.33x faster                                                             |
| json_loads           | 28.7 us                                                | 24.4 us: 1.18x faster                                                             |
| xml_etree_generate   | 93.8 ms                                                | 81.4 ms: 1.15x faster                                                             |
| pickle_list          | 4.72 us                                                | 4.17 us: 1.13x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 99.0 ms: 1.12x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                                             |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                                             |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                                             |
| pickle_dict          | 27.6 us                                                | 31.6 us: 1.14x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.00 ms: 1.56x faster                                                             |
| python_startup_no_site | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.93 ms: 1.48x faster                                                             |
| genshi_text     | 30.6 ms                                                | 21.7 ms: 1.41x faster                                                             |
| django_template | 46.3 ms                                                | 33.9 ms: 1.37x faster                                                             |
| genshi_xml      | 63.7 ms                                                | 48.7 ms: 1.31x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.7 ms: 2.49x faster                                                             |
| deltablue               | 7.28 ms                                                | 3.25 ms: 2.24x faster                                                             |
| logging_silent          | 176 ns                                                 | 93.8 ns: 1.88x faster                                                             |
| asyncio_tcp             | 914 ms                                                 | 499 ms: 1.83x faster                                                              |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                                              |
| richards                | 75.2 ms                                                | 44.3 ms: 1.70x faster                                                             |
| pyflate                 | 676 ms                                                 | 413 ms: 1.64x faster                                                              |
| go                      | 226 ms                                                 | 138 ms: 1.63x faster                                                              |
| scimark_monte_carlo     | 109 ms                                                 | 66.7 ms: 1.63x faster                                                             |
| raytrace                | 467 ms                                                 | 293 ms: 1.59x faster                                                              |
| crypto_pyaes            | 117 ms                                                 | 73.9 ms: 1.58x faster                                                             |
| chaos                   | 106 ms                                                 | 67.2 ms: 1.57x faster                                                             |
| python_startup          | 14.1 ms                                                | 9.00 ms: 1.56x faster                                                             |
| spectral_norm           | 150 ms                                                 | 95.8 ms: 1.56x faster                                                             |
| nbody                   | 144 ms                                                 | 92.4 ms: 1.56x faster                                                             |
| pickle_pure_python      | 452 us                                                 | 293 us: 1.54x faster                                                              |
| hexiom                  | 9.43 ms                                                | 6.25 ms: 1.51x faster                                                             |
| deepcopy_memo           | 51.7 us                                                | 34.6 us: 1.49x faster                                                             |
| unpickle_pure_python    | 302 us                                                 | 203 us: 1.49x faster                                                              |
| float                   | 109 ms                                                 | 73.4 ms: 1.48x faster                                                             |
| mako                    | 14.7 ms                                                | 9.93 ms: 1.48x faster                                                             |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                              |
| chameleon               | 9.17 ms                                                | 6.44 ms: 1.42x faster                                                             |
| json_dumps              | 13.4 ms                                                | 9.47 ms: 1.42x faster                                                             |
| unpack_sequence         | 59.4 ns                                                | 41.9 ns: 1.42x faster                                                             |
| genshi_text             | 30.6 ms                                                | 21.7 ms: 1.41x faster                                                             |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                                            |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                             |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.75 ms: 1.39x faster                                                             |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.39x faster                                                             |
| logging_format          | 8.85 us                                                | 6.41 us: 1.38x faster                                                             |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.38x faster                                                            |
| logging_simple          | 8.10 us                                                | 5.89 us: 1.37x faster                                                             |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                            |
| django_template         | 46.3 ms                                                | 33.9 ms: 1.37x faster                                                             |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                                              |
| scimark_fft             | 421 ms                                                 | 310 ms: 1.36x faster                                                              |
| coroutines              | 31.6 ms                                                | 23.3 ms: 1.36x faster                                                             |
| tornado_http            | 128 ms                                                 | 95.3 ms: 1.34x faster                                                             |
| fannkuch                | 488 ms                                                 | 365 ms: 1.33x faster                                                              |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                              |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                             |
| xml_etree_process       | 74.5 ms                                                | 56.1 ms: 1.33x faster                                                             |
| thrift                  | 1.03 ms                                                | 781 us: 1.32x faster                                                              |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                              |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                             |
| genshi_xml              | 63.7 ms                                                | 48.7 ms: 1.31x faster                                                             |
| async_tree_memoization  | 855 ms                                                 | 659 ms: 1.30x faster                                                              |
| deepcopy                | 438 us                                                 | 339 us: 1.29x faster                                                              |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.29x faster                                                              |
| mypy2                   | 430 ms                                                 | 335 ms: 1.28x faster                                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 742 ms: 1.28x faster                                                              |
| sqlglot_optimize        | 65.2 ms                                                | 51.3 ms: 1.27x faster                                                             |
| deepcopy_reduce         | 3.79 us                                                | 3.02 us: 1.25x faster                                                             |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.25x faster                                                            |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.56 ms: 1.20x faster                                                             |
| bench_thread_pool       | 946 us                                                 | 798 us: 1.19x faster                                                              |
| dulwich_log             | 75.8 ms                                                | 64.0 ms: 1.18x faster                                                             |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.2 ms: 1.18x faster                                                             |
| json_loads              | 28.7 us                                                | 24.4 us: 1.18x faster                                                             |
| sympy_integrate         | 24.0 ms                                                | 20.7 ms: 1.16x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                             |
| xml_etree_generate      | 93.8 ms                                                | 81.4 ms: 1.15x faster                                                             |
| json                    | 5.35 ms                                                | 4.68 ms: 1.14x faster                                                             |
| sympy_expand            | 534 ms                                                 | 469 ms: 1.14x faster                                                              |
| pickle_list             | 4.72 us                                                | 4.17 us: 1.13x faster                                                             |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                                             |
| sympy_str               | 325 ms                                                 | 289 ms: 1.12x faster                                                              |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.12x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 99.0 ms: 1.12x faster                                                             |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                             |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.47 sec: 1.11x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                              |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                              |
| sympy_sum               | 183 ms                                                 | 169 ms: 1.09x faster                                                              |
| telco                   | 6.73 ms                                                | 6.34 ms: 1.06x faster                                                             |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                                             |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                                              |
| async_generators        | 426 ms                                                 | 418 ms: 1.02x faster                                                              |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                                             |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                                             |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                              |
| python_startup_no_site  | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                             |
| pickle_dict             | 27.6 us                                                | 31.6 us: 1.14x slower                                                             |
| regex_effbot            | 3.19 ms                                                | 3.67 ms: 1.15x slower                                                             |
| dask                    | 436 ms                                                 | 511 ms: 1.17x slower                                                              |
| gc_traversal            | 3.53 ms                                                | 4.31 ms: 1.22x slower                                                             |
| coverage                | 74.7 ms                                                | 96.7 ms: 1.29x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-969caba/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba.json: comprehensions
