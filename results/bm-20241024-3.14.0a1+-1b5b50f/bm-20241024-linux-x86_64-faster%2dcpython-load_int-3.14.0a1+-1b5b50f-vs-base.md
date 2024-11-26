# Results vs. base

- fork: faster-cpython
- ref: load_int
- machine: linux-x86_64
- commit hash: 1b5b50f
- commit date: 2024-10-24
- overall geometric mean: 1.005x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 254 ms: 1.00x faster                                                 |
| html5lib       | 63.7 ms                                                                | 63.1 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (3): docutils, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io              | 857 ms                                                                 | 838 ms: 1.02x faster                                                 |
| async_generators           | 439 ms                                                                 | 433 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                 | 564 ms: 1.02x slower                                                 |
| coroutines                 | 23.0 ms                                                                | 23.6 ms: 1.03x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_none, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 80.4 ms                                                                | 79.3 ms: 1.01x faster                                                |
| pidigits       | 188 ms                                                                 | 187 ms: 1.00x faster                                                 |
| nbody          | 95.5 ms                                                                | 96.0 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.78 ms                                                                | 3.61 ms: 1.05x faster                                                |
| regex_compile  | 129 ms                                                                 | 129 ms: 1.00x faster                                                 |
| regex_dna      | 216 ms                                                                 | 216 ms: 1.00x faster                                                 |
| regex_v8       | 25.1 ms                                                                | 25.0 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 221 us                                                                 | 216 us: 1.02x faster                                                 |
| json_dumps           | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                |
| json_loads           | 26.2 us                                                                | 26.1 us: 1.00x faster                                                |
| xml_etree_generate   | 86.4 ms                                                                | 86.1 ms: 1.00x faster                                                |
| xml_etree_iterparse  | 106 ms                                                                 | 107 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 11.8 ms                                                                | 11.7 ms: 1.00x faster                                                |
| python_startup_no_site | 7.04 ms                                                                | 7.02 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 51.3 ms                                                                | 52.1 ms: 1.02x slower                                                |
| genshi_text    | 22.8 ms                                                                | 23.2 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 2.69 sec                                                               | 2.51 sec: 1.07x faster                                               |
| pyflate                    | 473 ms                                                                 | 446 ms: 1.06x faster                                                 |
| scimark_fft                | 378 ms                                                                 | 358 ms: 1.05x faster                                                 |
| regex_effbot               | 3.78 ms                                                                | 3.61 ms: 1.05x faster                                                |
| logging_silent             | 107 ns                                                                 | 103 ns: 1.04x faster                                                 |
| scimark_sparse_mat_mult    | 5.02 ms                                                                | 4.84 ms: 1.04x faster                                                |
| scimark_sor                | 129 ms                                                                 | 124 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 70.6 ms                                                                | 68.4 ms: 1.03x faster                                                |
| coverage                   | 85.9 ms                                                                | 83.6 ms: 1.03x faster                                                |
| unpickle_pure_python       | 221 us                                                                 | 216 us: 1.02x faster                                                 |
| typing_runtime_protocols   | 164 us                                                                 | 160 us: 1.02x faster                                                 |
| async_tree_io              | 857 ms                                                                 | 838 ms: 1.02x faster                                                 |
| nqueens                    | 81.4 ms                                                                | 79.7 ms: 1.02x faster                                                |
| scimark_lu                 | 115 ms                                                                 | 113 ms: 1.02x faster                                                 |
| bpe_tokeniser              | 4.85 sec                                                               | 4.76 sec: 1.02x faster                                               |
| meteor_contest             | 108 ms                                                                 | 106 ms: 1.02x faster                                                 |
| deepcopy_reduce            | 2.74 us                                                                | 2.70 us: 1.01x faster                                                |
| float                      | 80.4 ms                                                                | 79.3 ms: 1.01x faster                                                |
| async_generators           | 439 ms                                                                 | 433 ms: 1.01x faster                                                 |
| go                         | 122 ms                                                                 | 121 ms: 1.01x faster                                                 |
| hexiom                     | 6.37 ms                                                                | 6.29 ms: 1.01x faster                                                |
| generators                 | 28.6 ms                                                                | 28.3 ms: 1.01x faster                                                |
| pprint_safe_repr           | 736 ms                                                                 | 728 ms: 1.01x faster                                                 |
| logging_format             | 6.17 us                                                                | 6.11 us: 1.01x faster                                                |
| deepcopy_memo              | 31.1 us                                                                | 30.8 us: 1.01x faster                                                |
| html5lib                   | 63.7 ms                                                                | 63.1 ms: 1.01x faster                                                |
| sqlglot_parse              | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                |
| chaos                      | 61.2 ms                                                                | 60.8 ms: 1.01x faster                                                |
| json_dumps                 | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                |
| bench_mp_pool              | 78.3 ms                                                                | 77.8 ms: 1.01x faster                                                |
| python_startup             | 11.8 ms                                                                | 11.7 ms: 1.00x faster                                                |
| 2to3                       | 255 ms                                                                 | 254 ms: 1.00x faster                                                 |
| pprint_pformat             | 1.50 sec                                                               | 1.50 sec: 1.00x faster                                               |
| raytrace                   | 274 ms                                                                 | 273 ms: 1.00x faster                                                 |
| deepcopy                   | 262 us                                                                 | 261 us: 1.00x faster                                                 |
| json_loads                 | 26.2 us                                                                | 26.1 us: 1.00x faster                                                |
| sqlglot_transpile          | 1.60 ms                                                                | 1.59 ms: 1.00x faster                                                |
| xml_etree_generate         | 86.4 ms                                                                | 86.1 ms: 1.00x faster                                                |
| python_startup_no_site     | 7.04 ms                                                                | 7.02 ms: 1.00x faster                                                |
| regex_compile              | 129 ms                                                                 | 129 ms: 1.00x faster                                                 |
| regex_dna                  | 216 ms                                                                 | 216 ms: 1.00x faster                                                 |
| regex_v8                   | 25.1 ms                                                                | 25.0 ms: 1.00x faster                                                |
| pidigits                   | 188 ms                                                                 | 187 ms: 1.00x faster                                                 |
| sqlalchemy_declarative     | 128 ms                                                                 | 128 ms: 1.00x slower                                                 |
| create_gc_cycles           | 2.66 ms                                                                | 2.66 ms: 1.00x slower                                                |
| sympy_integrate            | 19.8 ms                                                                | 19.9 ms: 1.00x slower                                                |
| nbody                      | 95.5 ms                                                                | 96.0 ms: 1.01x slower                                                |
| json                       | 4.79 ms                                                                | 4.83 ms: 1.01x slower                                                |
| dulwich_log                | 63.5 ms                                                                | 63.9 ms: 1.01x slower                                                |
| fannkuch                   | 403 ms                                                                 | 406 ms: 1.01x slower                                                 |
| comprehensions             | 16.7 us                                                                | 16.9 us: 1.01x slower                                                |
| logging_simple             | 5.55 us                                                                | 5.59 us: 1.01x slower                                                |
| xml_etree_iterparse        | 106 ms                                                                 | 107 ms: 1.01x slower                                                 |
| genshi_xml                 | 51.3 ms                                                                | 52.1 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                 | 564 ms: 1.02x slower                                                 |
| genshi_text                | 22.8 ms                                                                | 23.2 ms: 1.02x slower                                                |
| pathlib                    | 15.9 ms                                                                | 16.2 ms: 1.02x slower                                                |
| coroutines                 | 23.0 ms                                                                | 23.6 ms: 1.03x slower                                                |
| pycparser                  | 1.13 sec                                                               | 1.17 sec: 1.03x slower                                               |
| gc_traversal               | 4.38 ms                                                                | 4.70 ms: 1.07x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (31): xml_etree_parse, async_tree_memoization, sphinx, pylint, sympy_str, sqlalchemy_imperative, async_tree_none, spectral_norm, pickle_pure_python, sqlglot_normalize, deltablue, bench_thread_pool, asyncio_websockets, tornado_http, sqlglot_optimize, crypto_pyaes, docutils, richards_super, sympy_expand, async_tree_memoization_tg, mako, xml_etree_process, tomli_loads, sympy_sum, richards, async_tree_none_tg, thrift, async_tree_io_tg, django_template, telco, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.005x faster
# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x