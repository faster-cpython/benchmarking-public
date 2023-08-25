
# Results vs. 3.10.4

- fork: brandtbucher
- ref: de_epfreeze
- machine: linux-x86_64
- commit hash: 034e2bf
- commit date: 2023-03-16
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                |
| chameleon      | 9.06 ms                                                | 6.43 ms: 1.41x faster                                               |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                              |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                               |
| tornado_http   | 127 ms                                                 | 91.7 ms: 1.39x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.3 ms: 1.59x faster                                               |
| float          | 111 ms                                                 | 73.6 ms: 1.50x faster                                               |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                |
| regex_v8       | 25.0 ms                                                | 25.6 ms: 1.02x slower                                               |
| regex_effbot   | 3.23 ms                                                | 3.42 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.62x faster                                                |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.41 ms: 1.44x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 56.3 ms: 1.33x faster                                               |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                               |
| xml_etree_generate   | 94.2 ms                                                | 81.7 ms: 1.15x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| pickle_list          | 4.56 us                                                | 4.16 us: 1.10x faster                                               |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                               |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                               |
| unpickle_list        | 4.82 us                                                | 5.19 us: 1.08x slower                                               |
| pickle_dict          | 27.3 us                                                | 30.8 us: 1.13x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.50 ms: 1.49x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.47 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.2 ms: 1.44x faster                                               |
| genshi_text     | 30.3 ms                                                | 21.7 ms: 1.40x faster                                               |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                               |
| genshi_xml      | 63.3 ms                                                | 48.4 ms: 1.31x faster                                               |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.1 ms: 2.55x faster                                               |
| deltablue               | 7.42 ms                                                | 3.16 ms: 2.35x faster                                               |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                |
| logging_silent          | 175 ns                                                 | 96.1 ns: 1.82x faster                                               |
| asyncio_tcp             | 925 ms                                                 | 508 ms: 1.82x faster                                                |
| richards                | 74.9 ms                                                | 43.9 ms: 1.71x faster                                               |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                                |
| spectral_norm           | 150 ms                                                 | 90.3 ms: 1.66x faster                                               |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                |
| scimark_monte_carlo     | 108 ms                                                 | 66.8 ms: 1.62x faster                                               |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.62x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 74.2 ms: 1.60x faster                                               |
| pyflate                 | 673 ms                                                 | 423 ms: 1.59x faster                                                |
| nbody                   | 142 ms                                                 | 89.3 ms: 1.59x faster                                               |
| chaos                   | 106 ms                                                 | 67.2 ms: 1.58x faster                                               |
| hexiom                  | 9.53 ms                                                | 6.10 ms: 1.56x faster                                               |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                               |
| unpack_sequence         | 64.7 ns                                                | 42.4 ns: 1.53x faster                                               |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.52x faster                                                |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                |
| float                   | 111 ms                                                 | 73.6 ms: 1.50x faster                                               |
| python_startup          | 14.2 ms                                                | 9.50 ms: 1.49x faster                                               |
| coroutines              | 31.8 ms                                                | 22.0 ms: 1.45x faster                                               |
| mako                    | 14.8 ms                                                | 10.2 ms: 1.44x faster                                               |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.41 ms: 1.44x faster                                               |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                               |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.41x faster                                               |
| chameleon               | 9.06 ms                                                | 6.43 ms: 1.41x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 609 ms: 1.40x faster                                                |
| genshi_text             | 30.3 ms                                                | 21.7 ms: 1.40x faster                                               |
| pprint_safe_repr        | 955 ms                                                 | 685 ms: 1.39x faster                                                |
| tornado_http            | 127 ms                                                 | 91.7 ms: 1.39x faster                                               |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.38x faster                                                |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                               |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                               |
| logging_simple          | 8.07 us                                                | 5.88 us: 1.37x faster                                               |
| logging_format          | 8.91 us                                                | 6.54 us: 1.36x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                              |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                               |
| thrift                  | 1.03 ms                                                | 774 us: 1.34x faster                                                |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                                |
| async_tree_none         | 717 ms                                                 | 539 ms: 1.33x faster                                                |
| xml_etree_process       | 74.9 ms                                                | 56.3 ms: 1.33x faster                                               |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                |
| genshi_xml              | 63.3 ms                                                | 48.4 ms: 1.31x faster                                               |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                                |
| pycparser               | 1.50 sec                                               | 1.17 sec: 1.28x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.7 ms: 1.26x faster                                               |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.39 ms: 1.24x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.22x faster                                                |
| async_tree_cpu_io_mixed | 951 ms                                                 | 782 ms: 1.22x faster                                                |
| nqueens                 | 100 ms                                                 | 82.3 ms: 1.21x faster                                               |
| dulwich_log             | 75.9 ms                                                | 62.6 ms: 1.21x faster                                               |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.21x faster                                               |
| bench_thread_pool       | 947 us                                                 | 796 us: 1.19x faster                                                |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                               |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                               |
| mdp                     | 2.82 sec                                               | 2.39 sec: 1.18x faster                                              |
| sympy_expand            | 545 ms                                                 | 467 ms: 1.17x faster                                                |
| json                    | 5.42 ms                                                | 4.69 ms: 1.15x faster                                               |
| xml_etree_generate      | 94.2 ms                                                | 81.7 ms: 1.15x faster                                               |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                                |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                               |
| comprehensions          | 26.8 us                                                | 23.9 us: 1.12x faster                                               |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                               |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                |
| sqlite_synth            | 2.93 us                                                | 2.64 us: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                               |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                |
| pickle_list             | 4.56 us                                                | 4.16 us: 1.10x faster                                               |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                |
| gc_traversal            | 3.84 ms                                                | 3.55 ms: 1.08x faster                                               |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                               |
| async_generators        | 425 ms                                                 | 416 ms: 1.02x faster                                                |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                               |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                |
| regex_v8                | 25.0 ms                                                | 25.6 ms: 1.02x slower                                               |
| regex_effbot            | 3.23 ms                                                | 3.42 ms: 1.06x slower                                               |
| unpickle_list           | 4.82 us                                                | 5.19 us: 1.08x slower                                               |
| python_startup_no_site  | 5.82 ms                                                | 6.47 ms: 1.11x slower                                               |
| pickle_dict             | 27.3 us                                                | 30.8 us: 1.13x slower                                               |
| dask                    | 423 ms                                                 | 511 ms: 1.21x slower                                                |
| coverage                | 72.8 ms                                                | 90.3 ms: 1.24x slower                                               |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (3): bench_mp_pool, telco, mypy2
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
