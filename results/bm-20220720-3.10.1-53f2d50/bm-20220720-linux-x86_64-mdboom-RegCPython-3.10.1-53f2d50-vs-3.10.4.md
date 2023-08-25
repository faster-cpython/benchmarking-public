
# Results vs. 3.10.4

- fork: mdboom
- ref: RegCPython
- machine: linux-x86_64
- commit hash: 53f2d50
- commit date: 2022-07-20
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 313 ms: 1.07x faster                                      |
| chameleon      | 9.06 ms                                                | 8.49 ms: 1.07x faster                                     |
| docutils       | 3.17 sec                                               | 3.10 sec: 1.02x faster                                    |
| html5lib       | 85.9 ms                                                | 76.8 ms: 1.12x faster                                     |
| tornado_http   | 127 ms                                                 | 123 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| nbody          | 142 ms                                                 | 101 ms: 1.40x faster                                      |
| float          | 111 ms                                                 | 94.9 ms: 1.16x faster                                     |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.18x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 157 ms: 1.13x faster                                      |
| regex_dna      | 222 ms                                                 | 216 ms: 1.03x faster                                      |
| regex_v8       | 25.0 ms                                                | 25.3 ms: 1.01x slower                                     |
| regex_effbot   | 3.23 ms                                                | 3.31 ms: 1.03x slower                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| xml_etree_generate   | 94.2 ms                                                | 86.2 ms: 1.09x faster                                     |
| xml_etree_process    | 74.9 ms                                                | 68.9 ms: 1.09x faster                                     |
| unpickle_pure_python | 300 us                                                 | 279 us: 1.08x faster                                      |
| pickle_pure_python   | 455 us                                                 | 432 us: 1.05x faster                                      |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                      |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.04x faster                                      |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                     |
| json_dumps           | 13.5 ms                                                | 13.4 ms: 1.01x faster                                     |
| json_loads           | 28.8 us                                                | 29.0 us: 1.01x slower                                     |
| unpickle_list        | 4.82 us                                                | 4.86 us: 1.01x slower                                     |
| pickle_list          | 4.56 us                                                | 4.65 us: 1.02x slower                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                              |

Benchmark hidden because not significant (2): pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup_no_site | 5.82 ms                                                | 5.80 ms: 1.00x faster                                     |
| python_startup         | 14.2 ms                                                | 15.2 ms: 1.07x slower                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 14.8 ms                                                | 13.1 ms: 1.13x faster                                     |
| genshi_text     | 30.3 ms                                                | 29.0 ms: 1.05x faster                                     |
| genshi_xml      | 63.3 ms                                                | 60.6 ms: 1.04x faster                                     |
| django_template | 45.9 ms                                                | 48.4 ms: 1.05x slower                                     |
| Geometric mean  | (ref)                                                  | 1.04x faster                                              |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| nbody                   | 142 ms                                                 | 101 ms: 1.40x faster                                      |
| generators              | 76.8 ms                                                | 56.3 ms: 1.36x faster                                     |
| fannkuch                | 486 ms                                                 | 369 ms: 1.32x faster                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.29 ms: 1.27x faster                                     |
| scimark_monte_carlo     | 108 ms                                                 | 85.8 ms: 1.26x faster                                     |
| scimark_fft             | 424 ms                                                 | 337 ms: 1.26x faster                                      |
| unpack_sequence         | 64.7 ns                                                | 52.8 ns: 1.23x faster                                     |
| spectral_norm           | 150 ms                                                 | 124 ms: 1.21x faster                                      |
| chaos                   | 106 ms                                                 | 91.1 ms: 1.17x faster                                     |
| float                   | 111 ms                                                 | 94.9 ms: 1.16x faster                                     |
| deepcopy_memo           | 52.3 us                                                | 45.1 us: 1.16x faster                                     |
| pyflate                 | 673 ms                                                 | 580 ms: 1.16x faster                                      |
| go                      | 229 ms                                                 | 203 ms: 1.13x faster                                      |
| hexiom                  | 9.53 ms                                                | 8.43 ms: 1.13x faster                                     |
| nqueens                 | 100 ms                                                 | 88.6 ms: 1.13x faster                                     |
| regex_compile           | 177 ms                                                 | 157 ms: 1.13x faster                                      |
| mako                    | 14.8 ms                                                | 13.1 ms: 1.13x faster                                     |
| crypto_pyaes            | 118 ms                                                 | 106 ms: 1.12x faster                                      |
| html5lib                | 85.9 ms                                                | 76.8 ms: 1.12x faster                                     |
| scimark_sor             | 197 ms                                                 | 176 ms: 1.11x faster                                      |
| coroutines              | 31.8 ms                                                | 28.6 ms: 1.11x faster                                     |
| richards                | 74.9 ms                                                | 67.6 ms: 1.11x faster                                     |
| aiohttp                 | 1.38 ms                                                | 1.25 ms: 1.11x faster                                     |
| async_tree_io           | 1.77 sec                                               | 1.61 sec: 1.10x faster                                    |
| gunicorn                | 1.46 ms                                                | 1.33 ms: 1.10x faster                                     |
| pycparser               | 1.50 sec                                               | 1.37 sec: 1.10x faster                                    |
| deepcopy                | 442 us                                                 | 404 us: 1.09x faster                                      |
| xml_etree_generate      | 94.2 ms                                                | 86.2 ms: 1.09x faster                                     |
| xml_etree_process       | 74.9 ms                                                | 68.9 ms: 1.09x faster                                     |
| deepcopy_reduce         | 3.82 us                                                | 3.55 us: 1.08x faster                                     |
| unpickle_pure_python    | 300 us                                                 | 279 us: 1.08x faster                                      |
| 2to3                    | 336 ms                                                 | 313 ms: 1.07x faster                                      |
| chameleon               | 9.06 ms                                                | 8.49 ms: 1.07x faster                                     |
| scimark_lu              | 163 ms                                                 | 153 ms: 1.07x faster                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.93 ms: 1.07x faster                                     |
| dulwich_log             | 75.9 ms                                                | 71.2 ms: 1.07x faster                                     |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.9 ms: 1.06x faster                                     |
| meteor_contest          | 115 ms                                                 | 108 ms: 1.06x faster                                      |
| sqlglot_transpile       | 2.45 ms                                                | 2.31 ms: 1.06x faster                                     |
| sympy_integrate         | 24.3 ms                                                | 22.9 ms: 1.06x faster                                     |
| logging_format          | 8.91 us                                                | 8.42 us: 1.06x faster                                     |
| pprint_pformat          | 1.99 sec                                               | 1.88 sec: 1.05x faster                                    |
| pickle_pure_python      | 455 us                                                 | 432 us: 1.05x faster                                      |
| raytrace                | 464 ms                                                 | 440 ms: 1.05x faster                                      |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                      |
| genshi_text             | 30.3 ms                                                | 29.0 ms: 1.05x faster                                     |
| asyncio_tcp             | 925 ms                                                 | 885 ms: 1.05x faster                                      |
| pprint_safe_repr        | 955 ms                                                 | 914 ms: 1.04x faster                                      |
| genshi_xml              | 63.3 ms                                                | 60.6 ms: 1.04x faster                                     |
| telco                   | 6.54 ms                                                | 6.27 ms: 1.04x faster                                     |
| sympy_str               | 328 ms                                                 | 316 ms: 1.04x faster                                      |
| tornado_http            | 127 ms                                                 | 123 ms: 1.04x faster                                      |
| xml_etree_parse         | 163 ms                                                 | 158 ms: 1.04x faster                                      |
| mdp                     | 2.82 sec                                               | 2.74 sec: 1.03x faster                                    |
| regex_dna               | 222 ms                                                 | 216 ms: 1.03x faster                                      |
| pylint                  | 525 ms                                                 | 512 ms: 1.03x faster                                      |
| deltablue               | 7.42 ms                                                | 7.24 ms: 1.03x faster                                     |
| flaskblogging           | 8.27 ms                                                | 8.07 ms: 1.02x faster                                     |
| docutils                | 3.17 sec                                               | 3.10 sec: 1.02x faster                                    |
| sympy_expand            | 545 ms                                                 | 533 ms: 1.02x faster                                      |
| logging_simple          | 8.07 us                                                | 7.90 us: 1.02x faster                                     |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                     |
| sympy_sum               | 185 ms                                                 | 181 ms: 1.02x faster                                      |
| async_tree_memoization  | 854 ms                                                 | 839 ms: 1.02x faster                                      |
| json_dumps              | 13.5 ms                                                | 13.4 ms: 1.01x faster                                     |
| sqlalchemy_declarative  | 165 ms                                                 | 164 ms: 1.01x faster                                      |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                      |
| json                    | 5.42 ms                                                | 5.37 ms: 1.01x faster                                     |
| gc_traversal            | 3.84 ms                                                | 3.83 ms: 1.00x faster                                     |
| python_startup_no_site  | 5.82 ms                                                | 5.80 ms: 1.00x faster                                     |
| json_loads              | 28.8 us                                                | 29.0 us: 1.01x slower                                     |
| unpickle_list           | 4.82 us                                                | 4.86 us: 1.01x slower                                     |
| regex_v8                | 25.0 ms                                                | 25.3 ms: 1.01x slower                                     |
| create_gc_cycles        | 1.67 ms                                                | 1.69 ms: 1.01x slower                                     |
| sqlglot_optimize        | 65.3 ms                                                | 66.5 ms: 1.02x slower                                     |
| pickle_list             | 4.56 us                                                | 4.65 us: 1.02x slower                                     |
| async_tree_cpu_io_mixed | 951 ms                                                 | 970 ms: 1.02x slower                                      |
| regex_effbot            | 3.23 ms                                                | 3.31 ms: 1.03x slower                                     |
| sqlglot_normalize       | 135 ms                                                 | 139 ms: 1.03x slower                                      |
| django_template         | 45.9 ms                                                | 48.4 ms: 1.05x slower                                     |
| python_startup          | 14.2 ms                                                | 15.2 ms: 1.07x slower                                     |
| logging_silent          | 175 ns                                                 | 194 ns: 1.11x slower                                      |
| async_generators        | 425 ms                                                 | 495 ms: 1.16x slower                                      |
| Geometric mean          | (ref)                                                  | 1.06x faster                                              |

Benchmark hidden because not significant (9): thrift, sqlite_synth, pickle_dict, bench_thread_pool, bench_mp_pool, pathlib, djangocms, async_tree_none, unpickle
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, coverage, dask, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220720-3.10.1-53f2d50/bm-20220720-linux-x86_64-mdboom-RegCPython-3.10.1-53f2d50.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
