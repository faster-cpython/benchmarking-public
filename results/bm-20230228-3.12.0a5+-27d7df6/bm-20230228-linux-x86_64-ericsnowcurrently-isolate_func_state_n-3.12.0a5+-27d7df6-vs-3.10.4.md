
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_func_state_n
- machine: linux-x86_64
- commit hash: 27d7df6
- commit date: 2023-02-28
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.33x faster                                                              |
| chameleon      | 9.17 ms                                                | 6.34 ms: 1.45x faster                                                             |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                            |
| html5lib       | 85.9 ms                                                | 62.4 ms: 1.37x faster                                                             |
| tornado_http   | 128 ms                                                 | 95.2 ms: 1.35x faster                                                             |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.1 ms: 1.53x faster                                                             |
| float          | 109 ms                                                 | 74.1 ms: 1.47x faster                                                             |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.31x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                             |
| regex_dna      | 214 ms                                                 | 199 ms: 1.07x faster                                                              |
| regex_effbot   | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 293 us: 1.54x faster                                                              |
| unpickle_pure_python | 302 us                                                 | 202 us: 1.49x faster                                                              |
| json_dumps           | 13.4 ms                                                | 9.58 ms: 1.40x faster                                                             |
| xml_etree_process    | 74.5 ms                                                | 56.4 ms: 1.32x faster                                                             |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                                             |
| pickle_list          | 4.72 us                                                | 4.07 us: 1.16x faster                                                             |
| xml_etree_generate   | 93.8 ms                                                | 81.7 ms: 1.15x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.08x faster                                                              |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.06x faster                                                              |
| unpickle             | 14.2 us                                                | 13.7 us: 1.03x faster                                                             |
| unpickle_list        | 4.92 us                                                | 4.99 us: 1.01x slower                                                             |
| pickle_dict          | 27.6 us                                                | 30.6 us: 1.11x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                      |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.04 ms: 1.56x faster                                                             |
| python_startup_no_site | 5.78 ms                                                | 6.56 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.88 ms: 1.48x faster                                                             |
| genshi_text     | 30.6 ms                                                | 21.8 ms: 1.41x faster                                                             |
| django_template | 46.3 ms                                                | 33.6 ms: 1.38x faster                                                             |
| genshi_xml      | 63.7 ms                                                | 49.0 ms: 1.30x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.8 ms: 2.48x faster                                                             |
| deltablue               | 7.28 ms                                                | 3.23 ms: 2.25x faster                                                             |
| logging_silent          | 176 ns                                                 | 94.0 ns: 1.88x faster                                                             |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                                              |
| asyncio_tcp             | 914 ms                                                 | 500 ms: 1.83x faster                                                              |
| richards                | 75.2 ms                                                | 43.9 ms: 1.71x faster                                                             |
| pyflate                 | 676 ms                                                 | 405 ms: 1.67x faster                                                              |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                                              |
| scimark_monte_carlo     | 109 ms                                                 | 66.6 ms: 1.63x faster                                                             |
| spectral_norm           | 150 ms                                                 | 93.0 ms: 1.61x faster                                                             |
| raytrace                | 467 ms                                                 | 291 ms: 1.60x faster                                                              |
| crypto_pyaes            | 117 ms                                                 | 74.2 ms: 1.57x faster                                                             |
| chaos                   | 106 ms                                                 | 67.7 ms: 1.56x faster                                                             |
| python_startup          | 14.1 ms                                                | 9.04 ms: 1.56x faster                                                             |
| pickle_pure_python      | 452 us                                                 | 293 us: 1.54x faster                                                              |
| hexiom                  | 9.43 ms                                                | 6.14 ms: 1.54x faster                                                             |
| nbody                   | 144 ms                                                 | 94.1 ms: 1.53x faster                                                             |
| unpickle_pure_python    | 302 us                                                 | 202 us: 1.49x faster                                                              |
| mako                    | 14.7 ms                                                | 9.88 ms: 1.48x faster                                                             |
| float                   | 109 ms                                                 | 74.1 ms: 1.47x faster                                                             |
| deepcopy_memo           | 51.7 us                                                | 35.4 us: 1.46x faster                                                             |
| chameleon               | 9.17 ms                                                | 6.34 ms: 1.45x faster                                                             |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.44x faster                                                              |
| unpack_sequence         | 59.4 ns                                                | 41.2 ns: 1.44x faster                                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.41x faster                                                             |
| genshi_text             | 30.6 ms                                                | 21.8 ms: 1.41x faster                                                             |
| json_dumps              | 13.4 ms                                                | 9.58 ms: 1.40x faster                                                             |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.39x faster                                                             |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.43 sec: 1.38x faster                                                            |
| django_template         | 46.3 ms                                                | 33.6 ms: 1.38x faster                                                             |
| html5lib                | 85.9 ms                                                | 62.4 ms: 1.37x faster                                                             |
| pprint_safe_repr        | 953 ms                                                 | 694 ms: 1.37x faster                                                              |
| logging_format          | 8.85 us                                                | 6.45 us: 1.37x faster                                                             |
| logging_simple          | 8.10 us                                                | 5.93 us: 1.37x faster                                                             |
| async_tree_none         | 711 ms                                                 | 521 ms: 1.36x faster                                                              |
| coroutines              | 31.6 ms                                                | 23.3 ms: 1.35x faster                                                             |
| scimark_fft             | 421 ms                                                 | 311 ms: 1.35x faster                                                              |
| tornado_http            | 128 ms                                                 | 95.2 ms: 1.35x faster                                                             |
| thrift                  | 1.03 ms                                                | 772 us: 1.34x faster                                                              |
| 2to3                    | 335 ms                                                 | 251 ms: 1.33x faster                                                              |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                             |
| fannkuch                | 488 ms                                                 | 367 ms: 1.33x faster                                                              |
| xml_etree_process       | 74.5 ms                                                | 56.4 ms: 1.32x faster                                                             |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                             |
| async_tree_memoization  | 855 ms                                                 | 653 ms: 1.31x faster                                                              |
| regex_compile           | 177 ms                                                 | 136 ms: 1.31x faster                                                              |
| genshi_xml              | 63.7 ms                                                | 49.0 ms: 1.30x faster                                                             |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                              |
| deepcopy                | 438 us                                                 | 340 us: 1.29x faster                                                              |
| mypy2                   | 430 ms                                                 | 335 ms: 1.28x faster                                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 741 ms: 1.28x faster                                                              |
| sqlglot_optimize        | 65.2 ms                                                | 51.3 ms: 1.27x faster                                                             |
| deepcopy_reduce         | 3.79 us                                                | 3.03 us: 1.25x faster                                                             |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.24x faster                                                            |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.44 ms: 1.23x faster                                                             |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                                             |
| dulwich_log             | 75.8 ms                                                | 63.4 ms: 1.20x faster                                                             |
| bench_thread_pool       | 946 us                                                 | 797 us: 1.19x faster                                                              |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.2 ms: 1.18x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 141 ms: 1.17x faster                                                              |
| sympy_integrate         | 24.0 ms                                                | 20.6 ms: 1.17x faster                                                             |
| pickle_list             | 4.72 us                                                | 4.07 us: 1.16x faster                                                             |
| djangocms               | 36.9 us                                                | 31.8 us: 1.16x faster                                                             |
| xml_etree_generate      | 93.8 ms                                                | 81.7 ms: 1.15x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                             |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                                             |
| sympy_expand            | 534 ms                                                 | 466 ms: 1.15x faster                                                              |
| sympy_str               | 325 ms                                                 | 287 ms: 1.13x faster                                                              |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                             |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.46 sec: 1.12x faster                                                            |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.51 ms: 1.09x faster                                                             |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.08x faster                                                              |
| regex_dna               | 214 ms                                                 | 199 ms: 1.07x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.06x faster                                                              |
| telco                   | 6.73 ms                                                | 6.45 ms: 1.04x faster                                                             |
| unpickle                | 14.2 us                                                | 13.7 us: 1.03x faster                                                             |
| async_generators        | 426 ms                                                 | 421 ms: 1.01x faster                                                              |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| unpickle_list           | 4.92 us                                                | 4.99 us: 1.01x slower                                                             |
| gc_traversal            | 3.53 ms                                                | 3.84 ms: 1.09x slower                                                             |
| pickle_dict             | 27.6 us                                                | 30.6 us: 1.11x slower                                                             |
| regex_effbot            | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.56 ms: 1.14x slower                                                             |
| dask                    | 436 ms                                                 | 508 ms: 1.16x slower                                                              |
| coverage                | 74.7 ms                                                | 98.3 ms: 1.31x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-27d7df6/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6.json: comprehensions
