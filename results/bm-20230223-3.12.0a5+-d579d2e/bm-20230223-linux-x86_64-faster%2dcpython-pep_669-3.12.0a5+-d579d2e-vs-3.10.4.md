
# Results vs. 3.10.4

- fork: faster-cpython
- ref: pep_669
- machine: linux-x86_64
- commit hash: d579d2e
- commit date: 2023-02-23
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 247 ms: 1.36x faster                                                |
| chameleon      | 9.06 ms                                                | 6.26 ms: 1.45x faster                                               |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                              |
| html5lib       | 85.9 ms                                                | 59.8 ms: 1.44x faster                                               |
| tornado_http   | 127 ms                                                 | 93.8 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.2 ms: 1.54x faster                                               |
| float          | 111 ms                                                 | 73.4 ms: 1.51x faster                                               |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                               |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 277 us: 1.64x faster                                                |
| unpickle_pure_python | 300 us                                                 | 194 us: 1.55x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.44x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 54.4 ms: 1.38x faster                                               |
| json_loads           | 28.8 us                                                | 23.7 us: 1.21x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 79.4 ms: 1.19x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 99.7 ms: 1.12x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| pickle_list          | 4.56 us                                                | 4.27 us: 1.07x faster                                               |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                               |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                               |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.06 ms: 1.56x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.58 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.75 ms: 1.51x faster                                               |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                               |
| django_template | 45.9 ms                                                | 32.8 ms: 1.40x faster                                               |
| genshi_xml      | 63.3 ms                                                | 45.9 ms: 1.38x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.6 ms: 2.43x faster                                               |
| deltablue               | 7.42 ms                                                | 3.14 ms: 2.37x faster                                               |
| logging_silent          | 175 ns                                                 | 91.7 ns: 1.91x faster                                               |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.90x faster                                                |
| asyncio_tcp             | 925 ms                                                 | 498 ms: 1.86x faster                                                |
| richards                | 74.9 ms                                                | 41.6 ms: 1.80x faster                                               |
| go                      | 229 ms                                                 | 130 ms: 1.76x faster                                                |
| scimark_monte_carlo     | 108 ms                                                 | 64.2 ms: 1.69x faster                                               |
| pyflate                 | 673 ms                                                 | 401 ms: 1.68x faster                                                |
| raytrace                | 464 ms                                                 | 280 ms: 1.66x faster                                                |
| pickle_pure_python      | 455 us                                                 | 277 us: 1.64x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 72.4 ms: 1.64x faster                                               |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.60x faster                                               |
| hexiom                  | 9.53 ms                                                | 6.00 ms: 1.59x faster                                               |
| spectral_norm           | 150 ms                                                 | 94.6 ms: 1.59x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 33.1 us: 1.58x faster                                               |
| python_startup          | 14.2 ms                                                | 9.06 ms: 1.56x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 194 us: 1.55x faster                                                |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                |
| nbody                   | 142 ms                                                 | 92.2 ms: 1.54x faster                                               |
| mako                    | 14.8 ms                                                | 9.75 ms: 1.51x faster                                               |
| float                   | 111 ms                                                 | 73.4 ms: 1.51x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 43.1 ns: 1.50x faster                                               |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.39 ms: 1.48x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.68 ms: 1.46x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                              |
| chameleon               | 9.06 ms                                                | 6.26 ms: 1.45x faster                                               |
| coroutines              | 31.8 ms                                                | 22.0 ms: 1.44x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 662 ms: 1.44x faster                                                |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.44x faster                                               |
| html5lib                | 85.9 ms                                                | 59.8 ms: 1.44x faster                                               |
| scimark_fft             | 424 ms                                                 | 302 ms: 1.40x faster                                                |
| django_template         | 45.9 ms                                                | 32.8 ms: 1.40x faster                                               |
| logging_simple          | 8.07 us                                                | 5.78 us: 1.40x faster                                               |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                               |
| logging_format          | 8.91 us                                                | 6.46 us: 1.38x faster                                               |
| genshi_xml              | 63.3 ms                                                | 45.9 ms: 1.38x faster                                               |
| xml_etree_process       | 74.9 ms                                                | 54.4 ms: 1.38x faster                                               |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.37x faster                                              |
| deepcopy                | 442 us                                                 | 323 us: 1.37x faster                                                |
| thrift                  | 1.03 ms                                                | 756 us: 1.37x faster                                                |
| fannkuch                | 486 ms                                                 | 357 ms: 1.36x faster                                                |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                |
| 2to3                    | 336 ms                                                 | 247 ms: 1.36x faster                                                |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                              |
| tornado_http            | 127 ms                                                 | 93.8 ms: 1.36x faster                                               |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.36x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 102 ms: 1.33x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                                |
| mypy2                   | 428 ms                                                 | 327 ms: 1.31x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 50.1 ms: 1.30x faster                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 741 ms: 1.28x faster                                                |
| nqueens                 | 100 ms                                                 | 78.4 ms: 1.28x faster                                               |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.34 ms: 1.25x faster                                               |
| dulwich_log             | 75.9 ms                                                | 61.6 ms: 1.23x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                |
| json_loads              | 28.8 us                                                | 23.7 us: 1.21x faster                                               |
| bench_thread_pool       | 947 us                                                 | 782 us: 1.21x faster                                                |
| sympy_expand            | 545 ms                                                 | 451 ms: 1.21x faster                                                |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.21x faster                                               |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                               |
| xml_etree_generate      | 94.2 ms                                                | 79.4 ms: 1.19x faster                                               |
| json                    | 5.42 ms                                                | 4.58 ms: 1.18x faster                                               |
| sympy_str               | 328 ms                                                 | 279 ms: 1.18x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                               |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.13x faster                                                |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 99.7 ms: 1.12x faster                                               |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                               |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                                |
| create_gc_cycles        | 1.67 ms                                                | 1.51 ms: 1.10x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.08x faster                                              |
| sqlite_synth            | 2.93 us                                                | 2.73 us: 1.08x faster                                               |
| pickle_list             | 4.56 us                                                | 4.27 us: 1.07x faster                                               |
| telco                   | 6.54 ms                                                | 6.35 ms: 1.03x faster                                               |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                               |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                               |
| async_generators        | 425 ms                                                 | 430 ms: 1.01x slower                                                |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| unpickle_list           | 4.82 us                                                | 4.98 us: 1.03x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.58 ms: 1.13x slower                                               |
| dask                    | 423 ms                                                 | 490 ms: 1.16x slower                                                |
| pickle_dict             | 27.3 us                                                | 31.7 us: 1.16x slower                                               |
| coverage                | 72.8 ms                                                | 96.9 ms: 1.33x slower                                               |
| Geometric mean          | (ref)                                                  | 1.32x faster                                                        |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x
