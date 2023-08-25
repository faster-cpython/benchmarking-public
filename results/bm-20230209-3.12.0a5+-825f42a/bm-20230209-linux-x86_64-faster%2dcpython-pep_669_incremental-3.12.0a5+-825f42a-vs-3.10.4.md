
# Results vs. 3.10.4

- fork: faster-cpython
- ref: pep_669_incremental
- machine: linux-x86_64
- commit hash: 825f42a
- commit date: 2023-02-09
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 246 ms: 1.37x faster                                                            |
| chameleon      | 9.06 ms                                                | 6.23 ms: 1.45x faster                                                           |
| docutils       | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                          |
| html5lib       | 85.9 ms                                                | 58.7 ms: 1.46x faster                                                           |
| tornado_http   | 127 ms                                                 | 92.8 ms: 1.37x faster                                                           |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.7 ms: 1.56x faster                                                           |
| float          | 111 ms                                                 | 71.4 ms: 1.55x faster                                                           |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 124 ms: 1.43x faster                                                            |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                           |
| regex_dna      | 222 ms                                                 | 201 ms: 1.10x faster                                                            |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 279 us: 1.63x faster                                                            |
| unpickle_pure_python | 300 us                                                 | 194 us: 1.55x faster                                                            |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                                           |
| xml_etree_process    | 74.9 ms                                                | 55.1 ms: 1.36x faster                                                           |
| json_loads           | 28.8 us                                                | 23.7 us: 1.21x faster                                                           |
| xml_etree_generate   | 94.2 ms                                                | 79.6 ms: 1.18x faster                                                           |
| pickle_list          | 4.56 us                                                | 4.04 us: 1.13x faster                                                           |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                            |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                                           |
| pickle               | 10.3 us                                                | 10.0 us: 1.03x faster                                                           |
| unpickle_list        | 4.82 us                                                | 5.15 us: 1.07x slower                                                           |
| pickle_dict          | 27.3 us                                                | 29.4 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.94 ms: 1.58x faster                                                           |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.79 ms: 1.51x faster                                                           |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                           |
| django_template | 45.9 ms                                                | 32.2 ms: 1.43x faster                                                           |
| genshi_xml      | 63.3 ms                                                | 45.5 ms: 1.39x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.11 ms: 2.38x faster                                                           |
| scimark_sor             | 197 ms                                                 | 102 ms: 1.93x faster                                                            |
| logging_silent          | 175 ns                                                 | 93.1 ns: 1.88x faster                                                           |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                                            |
| richards                | 74.9 ms                                                | 41.2 ms: 1.82x faster                                                           |
| go                      | 229 ms                                                 | 129 ms: 1.78x faster                                                            |
| chaos                   | 106 ms                                                 | 62.6 ms: 1.70x faster                                                           |
| scimark_monte_carlo     | 108 ms                                                 | 63.8 ms: 1.70x faster                                                           |
| raytrace                | 464 ms                                                 | 276 ms: 1.68x faster                                                            |
| hexiom                  | 9.53 ms                                                | 5.79 ms: 1.65x faster                                                           |
| crypto_pyaes            | 118 ms                                                 | 72.1 ms: 1.64x faster                                                           |
| pyflate                 | 673 ms                                                 | 410 ms: 1.64x faster                                                            |
| pickle_pure_python      | 455 us                                                 | 279 us: 1.63x faster                                                            |
| spectral_norm           | 150 ms                                                 | 93.3 ms: 1.61x faster                                                           |
| scimark_lu              | 163 ms                                                 | 103 ms: 1.59x faster                                                            |
| python_startup          | 14.2 ms                                                | 8.94 ms: 1.58x faster                                                           |
| deepcopy_memo           | 52.3 us                                                | 33.3 us: 1.57x faster                                                           |
| nbody                   | 142 ms                                                 | 90.7 ms: 1.56x faster                                                           |
| unpack_sequence         | 64.7 ns                                                | 41.8 ns: 1.55x faster                                                           |
| unpickle_pure_python    | 300 us                                                 | 194 us: 1.55x faster                                                            |
| float                   | 111 ms                                                 | 71.4 ms: 1.55x faster                                                           |
| mako                    | 14.8 ms                                                | 9.79 ms: 1.51x faster                                                           |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                           |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                           |
| html5lib                | 85.9 ms                                                | 58.7 ms: 1.46x faster                                                           |
| chameleon               | 9.06 ms                                                | 6.23 ms: 1.45x faster                                                           |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                           |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                          |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                                           |
| pprint_safe_repr        | 955 ms                                                 | 668 ms: 1.43x faster                                                            |
| logging_simple          | 8.07 us                                                | 5.65 us: 1.43x faster                                                           |
| regex_compile           | 177 ms                                                 | 124 ms: 1.43x faster                                                            |
| django_template         | 45.9 ms                                                | 32.2 ms: 1.43x faster                                                           |
| logging_format          | 8.91 us                                                | 6.26 us: 1.42x faster                                                           |
| scimark_fft             | 424 ms                                                 | 299 ms: 1.42x faster                                                            |
| aiohttp                 | 1.38 ms                                                | 983 us: 1.41x faster                                                            |
| generators              | 76.8 ms                                                | 54.8 ms: 1.40x faster                                                           |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.39x faster                                                          |
| genshi_xml              | 63.3 ms                                                | 45.5 ms: 1.39x faster                                                           |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.92 ms: 1.39x faster                                                           |
| gunicorn                | 1.46 ms                                                | 1.05 ms: 1.38x faster                                                           |
| deepcopy                | 442 us                                                 | 321 us: 1.38x faster                                                            |
| tornado_http            | 127 ms                                                 | 92.8 ms: 1.37x faster                                                           |
| 2to3                    | 336 ms                                                 | 246 ms: 1.37x faster                                                            |
| xml_etree_process       | 74.9 ms                                                | 55.1 ms: 1.36x faster                                                           |
| thrift                  | 1.03 ms                                                | 762 us: 1.36x faster                                                            |
| async_tree_none         | 717 ms                                                 | 529 ms: 1.36x faster                                                            |
| fannkuch                | 486 ms                                                 | 361 ms: 1.35x faster                                                            |
| deepcopy_reduce         | 3.82 us                                                | 2.86 us: 1.34x faster                                                           |
| mypy2                   | 428 ms                                                 | 322 ms: 1.33x faster                                                            |
| async_tree_memoization  | 854 ms                                                 | 643 ms: 1.33x faster                                                            |
| sqlglot_normalize       | 135 ms                                                 | 102 ms: 1.33x faster                                                            |
| nqueens                 | 100 ms                                                 | 75.5 ms: 1.32x faster                                                           |
| async_tree_io           | 1.77 sec                                               | 1.34 sec: 1.32x faster                                                          |
| sqlglot_optimize        | 65.3 ms                                                | 49.8 ms: 1.31x faster                                                           |
| docutils                | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                          |
| sympy_integrate         | 24.3 ms                                                | 19.5 ms: 1.25x faster                                                           |
| async_tree_cpu_io_mixed | 951 ms                                                 | 767 ms: 1.24x faster                                                            |
| sympy_str               | 328 ms                                                 | 265 ms: 1.24x faster                                                            |
| sqlalchemy_declarative  | 165 ms                                                 | 134 ms: 1.23x faster                                                            |
| dulwich_log             | 75.9 ms                                                | 61.5 ms: 1.23x faster                                                           |
| bench_thread_pool       | 947 us                                                 | 771 us: 1.23x faster                                                            |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.3 ms: 1.23x faster                                                           |
| sympy_expand            | 545 ms                                                 | 446 ms: 1.22x faster                                                            |
| json_loads              | 28.8 us                                                | 23.7 us: 1.21x faster                                                           |
| sympy_sum               | 185 ms                                                 | 155 ms: 1.19x faster                                                            |
| json                    | 5.42 ms                                                | 4.56 ms: 1.19x faster                                                           |
| xml_etree_generate      | 94.2 ms                                                | 79.6 ms: 1.18x faster                                                           |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                           |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                           |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                           |
| pickle_list             | 4.56 us                                                | 4.04 us: 1.13x faster                                                           |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                           |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                                           |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                            |
| regex_dna               | 222 ms                                                 | 201 ms: 1.10x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                            |
| mdp                     | 2.82 sec                                               | 2.67 sec: 1.06x faster                                                          |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                                           |
| telco                   | 6.54 ms                                                | 6.35 ms: 1.03x faster                                                           |
| pickle                  | 10.3 us                                                | 10.0 us: 1.03x faster                                                           |
| async_generators        | 425 ms                                                 | 420 ms: 1.01x faster                                                            |
| gc_traversal            | 3.84 ms                                                | 3.80 ms: 1.01x faster                                                           |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                            |
| unpickle_list           | 4.82 us                                                | 5.15 us: 1.07x slower                                                           |
| pickle_dict             | 27.3 us                                                | 29.4 us: 1.08x slower                                                           |
| regex_effbot            | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                           |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                           |
| coverage                | 72.8 ms                                                | 97.7 ms: 1.34x slower                                                           |
| coroutines              | 31.8 ms                                                | 54.8 ms: 1.72x slower                                                           |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x
