
# Results vs. 3.10.4

- fork: faster-cpython
- ref: pep_669
- machine: linux-x86_64
- commit hash: 662c16c
- commit date: 2023-03-25
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 247 ms: 1.36x faster                                                |
| chameleon      | 9.06 ms                                                | 6.20 ms: 1.46x faster                                               |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                              |
| html5lib       | 85.9 ms                                                | 60.5 ms: 1.42x faster                                               |
| tornado_http   | 127 ms                                                 | 90.0 ms: 1.42x faster                                               |
| Geometric mean | (ref)                                                  | 1.38x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 84.3 ms: 1.68x faster                                               |
| float          | 111 ms                                                 | 71.2 ms: 1.55x faster                                               |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.38x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                               |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.47 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.62x faster                                                |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.53 ms: 1.42x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 54.8 ms: 1.37x faster                                               |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 79.2 ms: 1.19x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 99.1 ms: 1.12x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| pickle_list          | 4.56 us                                                | 4.22 us: 1.08x faster                                               |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                               |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.86 ms: 1.60x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.57 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.85 ms: 1.50x faster                                               |
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.48x faster                                               |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                               |
| genshi_xml      | 63.3 ms                                                | 46.0 ms: 1.38x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-faster%2dcpython-pep_669-3.12.0a6+-662c16c |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 27.5 ms: 2.79x faster                                               |
| deltablue               | 7.42 ms                                                | 3.15 ms: 2.35x faster                                               |
| logging_silent          | 175 ns                                                 | 92.5 ns: 1.89x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 501 ms: 1.85x faster                                                |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                |
| richards                | 74.9 ms                                                | 42.4 ms: 1.76x faster                                               |
| spectral_norm           | 150 ms                                                 | 88.8 ms: 1.69x faster                                               |
| nbody                   | 142 ms                                                 | 84.3 ms: 1.68x faster                                               |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                                |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                                |
| scimark_monte_carlo     | 108 ms                                                 | 65.2 ms: 1.66x faster                                               |
| pyflate                 | 673 ms                                                 | 406 ms: 1.66x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 72.7 ms: 1.63x faster                                               |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.62x faster                                                |
| hexiom                  | 9.53 ms                                                | 5.90 ms: 1.61x faster                                               |
| python_startup          | 14.2 ms                                                | 8.86 ms: 1.60x faster                                               |
| chaos                   | 106 ms                                                 | 66.6 ms: 1.60x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 33.3 us: 1.57x faster                                               |
| float                   | 111 ms                                                 | 71.2 ms: 1.55x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.52x faster                                                |
| unpack_sequence         | 64.7 ns                                                | 43.1 ns: 1.50x faster                                               |
| mako                    | 14.8 ms                                                | 9.85 ms: 1.50x faster                                               |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.48x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.48x faster                                               |
| chameleon               | 9.06 ms                                                | 6.20 ms: 1.46x faster                                               |
| sqlglot_transpile       | 2.45 ms                                                | 1.68 ms: 1.45x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                              |
| coroutines              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                               |
| logging_format          | 8.91 us                                                | 6.23 us: 1.43x faster                                               |
| logging_simple          | 8.07 us                                                | 5.68 us: 1.42x faster                                               |
| html5lib                | 85.9 ms                                                | 60.5 ms: 1.42x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.53 ms: 1.42x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 673 ms: 1.42x faster                                                |
| tornado_http            | 127 ms                                                 | 90.0 ms: 1.42x faster                                               |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                               |
| aiohttp                 | 1.38 ms                                                | 991 us: 1.40x faster                                                |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.39x faster                                              |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.38x faster                                                |
| deepcopy                | 442 us                                                 | 319 us: 1.38x faster                                                |
| async_tree_none         | 717 ms                                                 | 520 ms: 1.38x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 620 ms: 1.38x faster                                                |
| genshi_xml              | 63.3 ms                                                | 46.0 ms: 1.38x faster                                               |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                |
| xml_etree_process       | 74.9 ms                                                | 54.8 ms: 1.37x faster                                               |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                               |
| 2to3                    | 336 ms                                                 | 247 ms: 1.36x faster                                                |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                              |
| thrift                  | 1.03 ms                                                | 784 us: 1.32x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                               |
| mypy2                   | 428 ms                                                 | 326 ms: 1.31x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.31x faster                                                |
| async_tree_cpu_io_mixed | 951 ms                                                 | 731 ms: 1.30x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 50.4 ms: 1.30x faster                                               |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.24 ms: 1.29x faster                                               |
| fannkuch                | 486 ms                                                 | 381 ms: 1.28x faster                                                |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                              |
| nqueens                 | 100 ms                                                 | 80.1 ms: 1.25x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 133 ms: 1.24x faster                                                |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.1 ms: 1.24x faster                                               |
| dulwich_log             | 75.9 ms                                                | 62.1 ms: 1.22x faster                                               |
| bench_thread_pool       | 947 us                                                 | 779 us: 1.22x faster                                                |
| sympy_integrate         | 24.3 ms                                                | 20.0 ms: 1.21x faster                                               |
| sympy_expand            | 545 ms                                                 | 449 ms: 1.21x faster                                                |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                               |
| xml_etree_generate      | 94.2 ms                                                | 79.2 ms: 1.19x faster                                               |
| sympy_str               | 328 ms                                                 | 277 ms: 1.19x faster                                                |
| json                    | 5.42 ms                                                | 4.61 ms: 1.18x faster                                               |
| comprehensions          | 26.8 us                                                | 23.3 us: 1.15x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.4 ms: 1.15x faster                                               |
| sympy_sum               | 185 ms                                                 | 162 ms: 1.14x faster                                                |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 99.1 ms: 1.12x faster                                               |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                               |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                               |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                |
| pickle_list             | 4.56 us                                                | 4.22 us: 1.08x faster                                               |
| gc_traversal            | 3.84 ms                                                | 3.64 ms: 1.06x faster                                               |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                               |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                |
| async_generators        | 425 ms                                                 | 422 ms: 1.01x faster                                                |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.03x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.47 ms: 1.07x slower                                               |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.57 ms: 1.13x slower                                               |
| dask                    | 423 ms                                                 | 490 ms: 1.16x slower                                                |
| coverage                | 72.8 ms                                                | 96.7 ms: 1.33x slower                                               |
| Geometric mean          | (ref)                                                  | 1.32x faster                                                        |

Benchmark hidden because not significant (3): unpickle, bench_mp_pool, pickle
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x
