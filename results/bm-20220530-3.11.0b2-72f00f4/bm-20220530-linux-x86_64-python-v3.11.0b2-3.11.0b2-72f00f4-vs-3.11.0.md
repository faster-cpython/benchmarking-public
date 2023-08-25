
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b2
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.00x faster \*
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                       |
| chameleon      | 6.47 ms                                                | 6.62 ms: 1.02x slower                                      |
| docutils       | 2.63 sec                                               | 2.56 sec: 1.03x faster                                     |
| tornado_http   | 96.3 ms                                                | 94.9 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 77.2 ms                                                | 74.4 ms: 1.04x faster                                      |
| nbody          | 93.1 ms                                                | 92.0 ms: 1.01x faster                                      |
| pidigits       | 198 ms                                                 | 199 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.11 ms: 1.29x faster                                      |
| regex_dna      | 204 ms                                                 | 196 ms: 1.04x faster                                       |
| regex_v8       | 22.0 ms                                                | 22.0 ms: 1.00x faster                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 26.4 us: 1.18x faster                                      |
| pickle               | 10.1 us                                                | 9.44 us: 1.07x faster                                      |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                      |
| xml_etree_process    | 53.9 ms                                                | 53.4 ms: 1.01x faster                                      |
| unpickle_pure_python | 228 us                                                 | 227 us: 1.01x faster                                       |
| json_dumps           | 12.6 ms                                                | 12.8 ms: 1.01x slower                                      |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.02x slower                                       |
| unpickle_list        | 4.91 us                                                | 5.00 us: 1.02x slower                                      |
| pickle_list          | 4.11 us                                                | 4.30 us: 1.05x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (4): unpickle, pickle_pure_python, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.49 ms: 1.00x faster                                      |
| python_startup_no_site | 6.01 ms                                                | 5.99 ms: 1.00x faster                                      |
| Geometric mean         | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako           | 10.1 ms                                                | 9.96 ms: 1.01x faster                                      |
| genshi_xml     | 51.8 ms                                                | 52.4 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.11 ms: 1.29x faster                                      |
| pickle_dict             | 31.1 us                                                | 26.4 us: 1.18x faster                                      |
| pickle                  | 10.1 us                                                | 9.44 us: 1.07x faster                                      |
| json_loads              | 26.5 us                                                | 25.0 us: 1.06x faster                                      |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                      |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                      |
| gunicorn                | 1.18 ms                                                | 1.13 ms: 1.05x faster                                      |
| async_generators        | 368 ms                                                 | 354 ms: 1.04x faster                                       |
| aiohttp                 | 1.10 ms                                                | 1.06 ms: 1.04x faster                                      |
| json                    | 4.94 ms                                                | 4.75 ms: 1.04x faster                                      |
| regex_dna               | 204 ms                                                 | 196 ms: 1.04x faster                                       |
| float                   | 77.2 ms                                                | 74.4 ms: 1.04x faster                                      |
| asyncio_tcp             | 922 ms                                                 | 890 ms: 1.04x faster                                       |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                     |
| raytrace                | 297 ms                                                 | 287 ms: 1.03x faster                                       |
| sympy_sum               | 167 ms                                                 | 161 ms: 1.03x faster                                       |
| deepcopy_memo           | 37.0 us                                                | 35.9 us: 1.03x faster                                      |
| scimark_monte_carlo     | 68.1 ms                                                | 66.0 ms: 1.03x faster                                      |
| scimark_sor             | 118 ms                                                 | 115 ms: 1.03x faster                                       |
| spectral_norm           | 100 ms                                                 | 97.3 ms: 1.03x faster                                      |
| docutils                | 2.63 sec                                               | 2.56 sec: 1.03x faster                                     |
| richards                | 45.7 ms                                                | 44.5 ms: 1.03x faster                                      |
| chaos                   | 69.2 ms                                                | 67.3 ms: 1.03x faster                                      |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                       |
| hexiom                  | 6.37 ms                                                | 6.27 ms: 1.02x faster                                      |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.02x faster                                      |
| tornado_http            | 96.3 ms                                                | 94.9 ms: 1.01x faster                                      |
| pyflate                 | 418 ms                                                 | 413 ms: 1.01x faster                                       |
| mako                    | 10.1 ms                                                | 9.96 ms: 1.01x faster                                      |
| nbody                   | 93.1 ms                                                | 92.0 ms: 1.01x faster                                      |
| 2to3                    | 259 ms                                                 | 256 ms: 1.01x faster                                       |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                       |
| xml_etree_process       | 53.9 ms                                                | 53.4 ms: 1.01x faster                                      |
| bench_thread_pool       | 819 us                                                 | 811 us: 1.01x faster                                       |
| thrift                  | 756 us                                                 | 750 us: 1.01x faster                                       |
| dulwich_log             | 63.7 ms                                                | 63.1 ms: 1.01x faster                                      |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                      |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                       |
| sympy_str               | 290 ms                                                 | 288 ms: 1.01x faster                                       |
| deepcopy                | 342 us                                                 | 340 us: 1.01x faster                                       |
| unpickle_pure_python    | 228 us                                                 | 227 us: 1.01x faster                                       |
| pprint_pformat          | 1.46 sec                                               | 1.45 sec: 1.01x faster                                     |
| regex_v8                | 22.0 ms                                                | 22.0 ms: 1.00x faster                                      |
| python_startup          | 8.52 ms                                                | 8.49 ms: 1.00x faster                                      |
| python_startup_no_site  | 6.01 ms                                                | 5.99 ms: 1.00x faster                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 743 ms: 1.01x slower                                       |
| pidigits                | 198 ms                                                 | 199 ms: 1.01x slower                                       |
| coroutines              | 25.5 ms                                                | 25.7 ms: 1.01x slower                                      |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                     |
| nqueens                 | 83.4 ms                                                | 84.2 ms: 1.01x slower                                      |
| genshi_xml              | 51.8 ms                                                | 52.4 ms: 1.01x slower                                      |
| generators              | 73.5 ms                                                | 74.4 ms: 1.01x slower                                      |
| json_dumps              | 12.6 ms                                                | 12.8 ms: 1.01x slower                                      |
| sqlglot_optimize        | 53.1 ms                                                | 53.9 ms: 1.01x slower                                      |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.02x slower                                       |
| logging_silent          | 101 ns                                                 | 103 ns: 1.02x slower                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.51 ms: 1.02x slower                                      |
| unpickle_list           | 4.91 us                                                | 5.00 us: 1.02x slower                                      |
| sqlglot_normalize       | 108 ms                                                 | 110 ms: 1.02x slower                                       |
| dask                    | 360 ms                                                 | 368 ms: 1.02x slower                                       |
| mdp                     | 2.62 sec                                               | 2.67 sec: 1.02x slower                                     |
| chameleon               | 6.47 ms                                                | 6.62 ms: 1.02x slower                                      |
| deepcopy_reduce         | 2.94 us                                                | 3.03 us: 1.03x slower                                      |
| djangocms               | 32.4 us                                                | 33.5 us: 1.03x slower                                      |
| fannkuch                | 388 ms                                                 | 403 ms: 1.04x slower                                       |
| pickle_list             | 4.11 us                                                | 4.30 us: 1.05x slower                                      |
| deltablue               | 3.67 ms                                                | 3.84 ms: 1.05x slower                                      |
| gc_traversal            | 4.02 ms                                                | 4.21 ms: 1.05x slower                                      |
| unpack_sequence         | 43.1 ns                                                | 46.2 ns: 1.07x slower                                      |
| comprehensions          | 22.4 us                                                | 26.0 us: 1.16x slower                                      |
| sqlglot_transpile       | 1.70 ms                                                | 2.05 ms: 1.20x slower                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.75 ms: 1.25x slower                                      |
| Geometric mean          | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (22): unpickle, html5lib, pylint, scimark_lu, telco, regex_compile, pickle_pure_python, pprint_safe_repr, xml_etree_generate, async_tree_none, django_template, mypy2, sqlalchemy_imperative, genshi_text, bench_mp_pool, sympy_expand, sqlite_synth, xml_etree_parse, crypto_pyaes, async_tree_memoization, scimark_fft, scimark_sparse_mat_mult
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
