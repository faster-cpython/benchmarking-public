# Results vs. 3.13.0

- fork: faster-cpython
- ref: load_int
- machine: linux-x86_64
- commit hash: 1b5b50f
- commit date: 2024-10-24
- overall geometric mean: 1.01x slower
- HPT reliability: 73.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 254 ms: 1.04x faster                                                 |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                               |
| html5lib       | 64.5 ms                                                | 63.1 ms: 1.02x faster                                                |
| tornado_http   | 91.5 ms                                                | 90.1 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 384 ms: 1.21x faster                                                 |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 564 ms: 1.04x slower                                                 |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                |
| async_tree_io_tg           | 825 ms                                                 | 982 ms: 1.19x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed, asyncio_websockets, async_generators, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                 |
| float          | 78.5 ms                                                | 79.3 ms: 1.01x slower                                                |
| nbody          | 85.7 ms                                                | 96.0 ms: 1.12x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                 |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                 |
| regex_v8       | 25.3 ms                                                | 25.0 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_loads           | 27.0 us                                                | 26.1 us: 1.03x faster                                                |
| tomli_loads          | 2.11 sec                                               | 2.08 sec: 1.01x faster                                               |
| xml_etree_generate   | 87.0 ms                                                | 86.1 ms: 1.01x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 59.9 ms: 1.01x faster                                                |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                 |
| xml_etree_parse      | 156 ms                                                 | 158 ms: 1.01x slower                                                 |
| pickle_pure_python   | 300 us                                                 | 311 us: 1.03x slower                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 107 ms: 1.05x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.02 ms: 1.00x slower                                                |
| python_startup         | 10.6 ms                                                | 11.7 ms: 1.11x slower                                                |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 34.8 ms: 1.01x slower                                                |
| genshi_text     | 22.9 ms                                                | 23.2 ms: 1.01x slower                                                |
| genshi_xml      | 50.3 ms                                                | 52.1 ms: 1.04x slower                                                |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 261 us: 1.35x faster                                                 |
| deepcopy_memo              | 38.0 us                                                | 30.8 us: 1.23x faster                                                |
| async_tree_memoization_tg  | 465 ms                                                 | 384 ms: 1.21x faster                                                 |
| go                         | 142 ms                                                 | 121 ms: 1.17x faster                                                 |
| deepcopy_reduce            | 3.17 us                                                | 2.70 us: 1.17x faster                                                |
| mdp                        | 2.74 sec                                               | 2.51 sec: 1.09x faster                                               |
| async_tree_none            | 354 ms                                                 | 328 ms: 1.08x faster                                                 |
| json                       | 5.20 ms                                                | 4.83 ms: 1.08x faster                                                |
| regex_effbot               | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                 |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                |
| telco                      | 8.45 ms                                                | 8.04 ms: 1.05x faster                                                |
| 2to3                       | 265 ms                                                 | 254 ms: 1.04x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.84 ms: 1.04x faster                                                |
| json_loads                 | 27.0 us                                                | 26.1 us: 1.03x faster                                                |
| richards_super             | 54.4 ms                                                | 52.7 ms: 1.03x faster                                                |
| pyflate                    | 460 ms                                                 | 446 ms: 1.03x faster                                                 |
| scimark_fft                | 369 ms                                                 | 358 ms: 1.03x faster                                                 |
| richards                   | 48.1 ms                                                | 46.9 ms: 1.03x faster                                                |
| sympy_str                  | 274 ms                                                 | 267 ms: 1.03x faster                                                 |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                                |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                               |
| html5lib                   | 64.5 ms                                                | 63.1 ms: 1.02x faster                                                |
| pprint_safe_repr           | 744 ms                                                 | 728 ms: 1.02x faster                                                 |
| thrift                     | 796 us                                                 | 780 us: 1.02x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                 |
| regex_compile              | 131 ms                                                 | 129 ms: 1.02x faster                                                 |
| generators                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                 |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                 |
| tornado_http               | 91.5 ms                                                | 90.1 ms: 1.02x faster                                                |
| tomli_loads                | 2.11 sec                                               | 2.08 sec: 1.01x faster                                               |
| sympy_expand               | 462 ms                                                 | 455 ms: 1.01x faster                                                 |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.59 us: 1.01x faster                                                |
| nqueens                    | 80.6 ms                                                | 79.7 ms: 1.01x faster                                                |
| sqlglot_optimize           | 53.9 ms                                                | 53.3 ms: 1.01x faster                                                |
| xml_etree_generate         | 87.0 ms                                                | 86.1 ms: 1.01x faster                                                |
| pprint_pformat             | 1.51 sec                                               | 1.50 sec: 1.01x faster                                               |
| regex_v8                   | 25.3 ms                                                | 25.0 ms: 1.01x faster                                                |
| sqlglot_normalize          | 107 ms                                                 | 106 ms: 1.01x faster                                                 |
| xml_etree_process          | 60.4 ms                                                | 59.9 ms: 1.01x faster                                                |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x slower                                                 |
| python_startup_no_site     | 6.99 ms                                                | 7.02 ms: 1.00x slower                                                |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                 |
| crypto_pyaes               | 73.0 ms                                                | 73.6 ms: 1.01x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                 |
| float                      | 78.5 ms                                                | 79.3 ms: 1.01x slower                                                |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.01x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                |
| django_template            | 34.4 ms                                                | 34.8 ms: 1.01x slower                                                |
| genshi_text                | 22.9 ms                                                | 23.2 ms: 1.01x slower                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.76 sec: 1.02x slower                                               |
| dulwich_log                | 63.0 ms                                                | 63.9 ms: 1.02x slower                                                |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.02x slower                                                 |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                |
| hexiom                     | 6.13 ms                                                | 6.29 ms: 1.03x slower                                                |
| bench_thread_pool          | 815 us                                                 | 837 us: 1.03x slower                                                 |
| comprehensions             | 16.4 us                                                | 16.9 us: 1.03x slower                                                |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                               |
| scimark_monte_carlo        | 66.3 ms                                                | 68.4 ms: 1.03x slower                                                |
| pickle_pure_python         | 300 us                                                 | 311 us: 1.03x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 52.1 ms: 1.04x slower                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 564 ms: 1.04x slower                                                 |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                |
| chaos                      | 58.4 ms                                                | 60.8 ms: 1.04x slower                                                |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 107 ms: 1.05x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.30 ms: 1.05x slower                                                |
| coroutines                 | 22.5 ms                                                | 23.6 ms: 1.05x slower                                                |
| fannkuch                   | 381 ms                                                 | 406 ms: 1.07x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                |
| python_startup             | 10.6 ms                                                | 11.7 ms: 1.11x slower                                                |
| nbody                      | 85.7 ms                                                | 96.0 ms: 1.12x slower                                                |
| async_tree_io_tg           | 825 ms                                                 | 982 ms: 1.19x slower                                                 |
| gc_traversal               | 3.81 ms                                                | 4.70 ms: 1.23x slower                                                |
| create_gc_cycles           | 1.61 ms                                                | 2.66 ms: 1.66x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 77.8 ms: 3.24x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (10): async_tree_io, coverage, sympy_integrate, async_tree_cpu_io_mixed, asyncio_websockets, async_generators, typing_runtime_protocols, logging_silent, async_tree_none_tg, pylint
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (3) of results/bm-20241024-3.14.0a1+-1b5b50f/bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f.json: sphinx, sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 73.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x