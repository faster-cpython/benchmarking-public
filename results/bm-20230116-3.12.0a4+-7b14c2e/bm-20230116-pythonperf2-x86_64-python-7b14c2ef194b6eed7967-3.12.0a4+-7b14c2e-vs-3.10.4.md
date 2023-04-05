
# Results vs. 3.10.4

- fork: python
- ref: 7b14c2ef194b6eed7967
- machine: linux-x86_64
- commit hash: 7b14c2e
- commit date: 2023-01-16
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                       | 287 ms: 1.23x faster                                                         |
| chameleon      | 9.62 ms                                                      | 7.60 ms: 1.27x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| html5lib       | 96.3 ms                                                      | 66.6 ms: 1.45x faster                                                        |
| tornado_http   | 151 ms                                                       | 120 ms: 1.26x faster                                                         |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 109 ms                                                       | 72.6 ms: 1.51x faster                                                        |
| nbody          | 132 ms                                                       | 89.1 ms: 1.48x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 191 ms                                                       | 151 ms: 1.26x faster                                                         |
| regex_dna      | 261 ms                                                       | 226 ms: 1.16x faster                                                         |
| regex_v8       | 26.0 ms                                                      | 22.9 ms: 1.14x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.34 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 318 us                                                       | 210 us: 1.52x faster                                                         |
| pickle_pure_python   | 451 us                                                       | 304 us: 1.48x faster                                                         |
| xml_etree_process    | 77.6 ms                                                      | 54.8 ms: 1.41x faster                                                        |
| json_dumps           | 14.3 ms                                                      | 10.1 ms: 1.41x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.3 us: 1.25x faster                                                        |
| xml_etree_generate   | 94.1 ms                                                      | 79.0 ms: 1.19x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| unpickle_list        | 4.73 us                                                      | 4.53 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 109 ms                                                       | 106 ms: 1.03x faster                                                         |
| pickle               | 10.1 us                                                      | 10.0 us: 1.01x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 32.2 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.18 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                        |
| django_template | 52.0 ms                                                      | 40.0 ms: 1.30x faster                                                        |
| genshi_text     | 31.7 ms                                                      | 25.5 ms: 1.24x faster                                                        |
| genshi_xml      | 63.5 ms                                                      | 56.5 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-pythonperf2-x86_64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.54 ms                                                      | 3.58 ms: 2.11x faster                                                        |
| asyncio_tcp             | 787 ms                                                       | 393 ms: 2.00x faster                                                         |
| pyflate                 | 731 ms                                                       | 436 ms: 1.68x faster                                                         |
| logging_silent          | 165 ns                                                       | 99.5 ns: 1.65x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 65.8 ms: 1.65x faster                                                        |
| go                      | 264 ms                                                       | 160 ms: 1.65x faster                                                         |
| raytrace                | 491 ms                                                       | 300 ms: 1.64x faster                                                         |
| scimark_sor             | 177 ms                                                       | 109 ms: 1.62x faster                                                         |
| richards                | 73.9 ms                                                      | 46.0 ms: 1.61x faster                                                        |
| scimark_lu              | 164 ms                                                       | 103 ms: 1.60x faster                                                         |
| unpickle_pure_python    | 318 us                                                       | 210 us: 1.52x faster                                                         |
| float                   | 109 ms                                                       | 72.6 ms: 1.51x faster                                                        |
| chaos                   | 108 ms                                                       | 72.1 ms: 1.50x faster                                                        |
| pickle_pure_python      | 451 us                                                       | 304 us: 1.48x faster                                                         |
| nbody                   | 132 ms                                                       | 89.1 ms: 1.48x faster                                                        |
| bench_mp_pool           | 7.10 ms                                                      | 4.79 ms: 1.48x faster                                                        |
| html5lib                | 96.3 ms                                                      | 66.6 ms: 1.45x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.45x faster                                                        |
| hexiom                  | 9.54 ms                                                      | 6.69 ms: 1.43x faster                                                        |
| spectral_norm           | 138 ms                                                       | 96.9 ms: 1.42x faster                                                        |
| xml_etree_process       | 77.6 ms                                                      | 54.8 ms: 1.41x faster                                                        |
| sqlglot_parse           | 2.24 ms                                                      | 1.59 ms: 1.41x faster                                                        |
| json_dumps              | 14.3 ms                                                      | 10.1 ms: 1.41x faster                                                        |
| crypto_pyaes            | 119 ms                                                       | 84.3 ms: 1.41x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.16 sec: 1.39x faster                                                       |
| scimark_sparse_mat_mult | 5.09 ms                                                      | 3.66 ms: 1.39x faster                                                        |
| sqlglot_transpile       | 2.69 ms                                                      | 1.96 ms: 1.37x faster                                                        |
| async_tree_none         | 698 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_memoization  | 822 ms                                                       | 609 ms: 1.35x faster                                                         |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.34x faster                                                       |
| thrift                  | 1.23 ms                                                      | 916 us: 1.34x faster                                                         |
| unpack_sequence         | 59.7 ns                                                      | 44.7 ns: 1.34x faster                                                        |
| pprint_pformat          | 2.12 sec                                                     | 1.59 sec: 1.34x faster                                                       |
| deepcopy_memo           | 49.2 us                                                      | 37.1 us: 1.33x faster                                                        |
| pprint_safe_repr        | 1.03 sec                                                     | 774 ms: 1.33x faster                                                         |
| django_template         | 52.0 ms                                                      | 40.0 ms: 1.30x faster                                                        |
| logging_simple          | 9.24 us                                                      | 7.12 us: 1.30x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                       | 741 ms: 1.28x faster                                                         |
| aiohttp                 | 1.18 ms                                                      | 927 us: 1.27x faster                                                         |
| chameleon               | 9.62 ms                                                      | 7.60 ms: 1.27x faster                                                        |
| regex_compile           | 191 ms                                                       | 151 ms: 1.26x faster                                                         |
| async_generators        | 419 ms                                                       | 333 ms: 1.26x faster                                                         |
| logging_format          | 9.94 us                                                      | 7.90 us: 1.26x faster                                                        |
| tornado_http            | 151 ms                                                       | 120 ms: 1.26x faster                                                         |
| gunicorn                | 1.15 ms                                                      | 914 us: 1.25x faster                                                         |
| scimark_fft             | 359 ms                                                       | 287 ms: 1.25x faster                                                         |
| json_loads              | 30.3 us                                                      | 24.3 us: 1.25x faster                                                        |
| genshi_text             | 31.7 ms                                                      | 25.5 ms: 1.24x faster                                                        |
| fannkuch                | 496 ms                                                       | 401 ms: 1.24x faster                                                         |
| mypy2                   | 466 ms                                                       | 379 ms: 1.23x faster                                                         |
| docutils                | 3.41 sec                                                     | 2.78 sec: 1.23x faster                                                       |
| 2to3                    | 352 ms                                                       | 287 ms: 1.23x faster                                                         |
| sqlglot_normalize       | 147 ms                                                       | 122 ms: 1.21x faster                                                         |
| dulwich_log             | 80.5 ms                                                      | 66.9 ms: 1.20x faster                                                        |
| sqlglot_optimize        | 70.1 ms                                                      | 58.5 ms: 1.20x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 955 us: 1.19x faster                                                         |
| xml_etree_generate      | 94.1 ms                                                      | 79.0 ms: 1.19x faster                                                        |
| nqueens                 | 114 ms                                                       | 95.8 ms: 1.19x faster                                                        |
| json                    | 5.94 ms                                                      | 5.09 ms: 1.17x faster                                                        |
| regex_dna               | 261 ms                                                       | 226 ms: 1.16x faster                                                         |
| deepcopy                | 457 us                                                       | 397 us: 1.15x faster                                                         |
| sqlite_synth            | 2.96 us                                                      | 2.57 us: 1.15x faster                                                        |
| dask                    | 478 ms                                                       | 415 ms: 1.15x faster                                                         |
| regex_v8                | 26.0 ms                                                      | 22.9 ms: 1.14x faster                                                        |
| deepcopy_reduce         | 3.91 us                                                      | 3.45 us: 1.14x faster                                                        |
| create_gc_cycles        | 1.80 ms                                                      | 1.59 ms: 1.13x faster                                                        |
| sympy_expand            | 603 ms                                                       | 536 ms: 1.13x faster                                                         |
| genshi_xml              | 63.5 ms                                                      | 56.5 ms: 1.12x faster                                                        |
| xml_etree_parse         | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| sympy_integrate         | 28.1 ms                                                      | 25.4 ms: 1.11x faster                                                        |
| meteor_contest          | 142 ms                                                       | 129 ms: 1.10x faster                                                         |
| pathlib                 | 21.3 ms                                                      | 19.3 ms: 1.10x faster                                                        |
| coroutines              | 30.6 ms                                                      | 28.3 ms: 1.08x faster                                                        |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| sympy_str               | 358 ms                                                       | 333 ms: 1.07x faster                                                         |
| mdp                     | 2.95 sec                                                     | 2.77 sec: 1.07x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.77 ms: 1.05x faster                                                        |
| unpickle_list           | 4.73 us                                                      | 4.53 us: 1.04x faster                                                        |
| sympy_sum               | 193 ms                                                       | 185 ms: 1.04x faster                                                         |
| python_startup          | 11.5 ms                                                      | 11.1 ms: 1.03x faster                                                        |
| xml_etree_iterparse     | 109 ms                                                       | 106 ms: 1.03x faster                                                         |
| pickle                  | 10.1 us                                                      | 10.0 us: 1.01x faster                                                        |
| gc_traversal            | 3.46 ms                                                      | 3.52 ms: 1.02x slower                                                        |
| generators              | 57.0 ms                                                      | 60.7 ms: 1.06x slower                                                        |
| pickle_dict             | 29.5 us                                                      | 32.2 us: 1.09x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.18 ms: 1.12x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.34 ms: 1.12x slower                                                        |
| coverage                | 71.1 ms                                                      | 86.4 ms: 1.22x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                 |

Benchmark hidden because not significant (3): unpickle, pickle_list, comprehensions
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
