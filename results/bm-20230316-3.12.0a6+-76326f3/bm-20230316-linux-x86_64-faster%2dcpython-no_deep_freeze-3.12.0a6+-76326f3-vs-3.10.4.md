
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_deep_freeze
- machine: linux-x86_64
- commit hash: 76326f3
- commit date: 2023-03-16
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.34x faster                                                       |
| chameleon      | 9.06 ms                                                | 6.36 ms: 1.42x faster                                                      |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                     |
| html5lib       | 85.9 ms                                                | 59.2 ms: 1.45x faster                                                      |
| tornado_http   | 127 ms                                                 | 90.9 ms: 1.40x faster                                                      |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.2 ms: 1.61x faster                                                      |
| float          | 111 ms                                                 | 73.7 ms: 1.50x faster                                                      |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                       |
| regex_dna      | 222 ms                                                 | 204 ms: 1.08x faster                                                       |
| regex_v8       | 25.0 ms                                                | 25.6 ms: 1.02x slower                                                      |
| regex_effbot   | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                       |
| json_dumps           | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 56.4 ms: 1.33x faster                                                      |
| json_loads           | 28.8 us                                                | 23.9 us: 1.20x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 81.8 ms: 1.15x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 99.7 ms: 1.12x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                                       |
| pickle_list          | 4.56 us                                                | 4.21 us: 1.08x faster                                                      |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                      |
| pickle_dict          | 27.3 us                                                | 30.0 us: 1.10x slower                                                      |
| unpickle_list        | 4.82 us                                                | 5.32 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.51 ms: 1.49x faster                                                      |
| python_startup_no_site | 5.82 ms                                                | 6.48 ms: 1.11x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.2 ms: 1.45x faster                                                      |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                      |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                      |
| genshi_xml      | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.9 ms: 2.56x faster                                                      |
| deltablue               | 7.42 ms                                                | 3.15 ms: 2.36x faster                                                      |
| logging_silent          | 175 ns                                                 | 93.4 ns: 1.87x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                       |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                                       |
| richards                | 74.9 ms                                                | 42.6 ms: 1.76x faster                                                      |
| go                      | 229 ms                                                 | 132 ms: 1.74x faster                                                       |
| spectral_norm           | 150 ms                                                 | 90.6 ms: 1.66x faster                                                      |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                                       |
| scimark_monte_carlo     | 108 ms                                                 | 67.0 ms: 1.62x faster                                                      |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                                       |
| nbody                   | 142 ms                                                 | 88.2 ms: 1.61x faster                                                      |
| chaos                   | 106 ms                                                 | 66.7 ms: 1.59x faster                                                      |
| crypto_pyaes            | 118 ms                                                 | 74.4 ms: 1.59x faster                                                      |
| pyflate                 | 673 ms                                                 | 423 ms: 1.59x faster                                                       |
| hexiom                  | 9.53 ms                                                | 6.10 ms: 1.56x faster                                                      |
| deepcopy_memo           | 52.3 us                                                | 33.7 us: 1.56x faster                                                      |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                       |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 42.8 ns: 1.51x faster                                                      |
| float                   | 111 ms                                                 | 73.7 ms: 1.50x faster                                                      |
| python_startup          | 14.2 ms                                                | 9.51 ms: 1.49x faster                                                      |
| html5lib                | 85.9 ms                                                | 59.2 ms: 1.45x faster                                                      |
| mako                    | 14.8 ms                                                | 10.2 ms: 1.45x faster                                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                                      |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                      |
| coroutines              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                      |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                      |
| chameleon               | 9.06 ms                                                | 6.36 ms: 1.42x faster                                                      |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                     |
| logging_simple          | 8.07 us                                                | 5.69 us: 1.42x faster                                                      |
| async_tree_memoization  | 854 ms                                                 | 606 ms: 1.41x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                      |
| logging_format          | 8.91 us                                                | 6.34 us: 1.41x faster                                                      |
| tornado_http            | 127 ms                                                 | 90.9 ms: 1.40x faster                                                      |
| scimark_fft             | 424 ms                                                 | 304 ms: 1.39x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 687 ms: 1.39x faster                                                       |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                      |
| aiohttp                 | 1.38 ms                                                | 996 us: 1.39x faster                                                       |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.36x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.36x faster                                                     |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                                       |
| async_tree_none         | 717 ms                                                 | 535 ms: 1.34x faster                                                       |
| thrift                  | 1.03 ms                                                | 772 us: 1.34x faster                                                       |
| 2to3                    | 336 ms                                                 | 252 ms: 1.34x faster                                                       |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 56.4 ms: 1.33x faster                                                      |
| genshi_xml              | 63.3 ms                                                | 47.7 ms: 1.33x faster                                                      |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                                       |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                                      |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                       |
| pycparser               | 1.50 sec                                               | 1.17 sec: 1.28x faster                                                     |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                                      |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.37 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed | 951 ms                                                 | 770 ms: 1.24x faster                                                       |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                                      |
| dulwich_log             | 75.9 ms                                                | 62.3 ms: 1.22x faster                                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                       |
| json_loads              | 28.8 us                                                | 23.9 us: 1.20x faster                                                      |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                       |
| json                    | 5.42 ms                                                | 4.54 ms: 1.19x faster                                                      |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                      |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.8 ms: 1.19x faster                                                      |
| mdp                     | 2.82 sec                                               | 2.40 sec: 1.18x faster                                                     |
| sympy_expand            | 545 ms                                                 | 464 ms: 1.17x faster                                                       |
| sympy_str               | 328 ms                                                 | 284 ms: 1.16x faster                                                       |
| xml_etree_generate      | 94.2 ms                                                | 81.8 ms: 1.15x faster                                                      |
| comprehensions          | 26.8 us                                                | 23.6 us: 1.14x faster                                                      |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 99.7 ms: 1.12x faster                                                      |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                       |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                      |
| sqlite_synth            | 2.93 us                                                | 2.65 us: 1.11x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                                       |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                       |
| regex_dna               | 222 ms                                                 | 204 ms: 1.08x faster                                                       |
| pickle_list             | 4.56 us                                                | 4.21 us: 1.08x faster                                                      |
| gc_traversal            | 3.84 ms                                                | 3.68 ms: 1.04x faster                                                      |
| async_generators        | 425 ms                                                 | 411 ms: 1.03x faster                                                       |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                      |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| regex_v8                | 25.0 ms                                                | 25.6 ms: 1.02x slower                                                      |
| regex_effbot            | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                      |
| pickle_dict             | 27.3 us                                                | 30.0 us: 1.10x slower                                                      |
| unpickle_list           | 4.82 us                                                | 5.32 us: 1.10x slower                                                      |
| python_startup_no_site  | 5.82 ms                                                | 6.48 ms: 1.11x slower                                                      |
| dask                    | 423 ms                                                 | 503 ms: 1.19x slower                                                       |
| coverage                | 72.8 ms                                                | 91.6 ms: 1.26x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (4): bench_mp_pool, telco, unpickle, mypy2
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
