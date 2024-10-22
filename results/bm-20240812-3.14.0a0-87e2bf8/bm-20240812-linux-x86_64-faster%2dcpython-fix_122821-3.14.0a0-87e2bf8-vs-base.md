# Results vs. base

- fork: faster-cpython
- ref: fix_122821
- machine: linux-x86_64
- commit hash: 87e2bf8
- commit date: 2024-08-12
- overall geometric mean: 1.01x slower
- HPT reliability: 99.17%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240811-linux-x86_64-python-253c6a0b2f88b3327b71-3.14.0a0-253c6a0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.71 sec                                                              | 2.73 sec: 1.01x slower                                                |
| html5lib       | 65.2 ms                                                               | 65.0 ms: 1.00x faster                                                 |
| tornado_http   | 90.0 ms                                                               | 90.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240811-linux-x86_64-python-253c6a0b2f88b3327b71-3.14.0a0-253c6a0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines         | 23.6 ms                                                               | 22.5 ms: 1.05x faster                                                 |
| async_tree_none_tg | 302 ms                                                                | 298 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl    | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                |
| asyncio_tcp        | 488 ms                                                                | 492 ms: 1.01x slower                                                  |
| async_generators   | 437 ms                                                                | 443 ms: 1.01x slower                                                  |
| Geometric mean     | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240811-linux-x86_64-python-253c6a0b2f88b3327b71-3.14.0a0-253c6a0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 88.2 ms                                                               | 87.7 ms: 1.01x faster                                                 |
| float          | 79.3 ms                                                               | 78.9 ms: 1.01x faster                                                 |
| pidigits       | 187 ms                                                                | 188 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240811-linux-x86_64-python-253c6a0b2f88b3327b71-3.14.0a0-253c6a0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                | 132 ms: 1.01x slower                                                  |
| regex_dna      | 222 ms                                                                | 227 ms: 1.02x slower                                                  |
| regex_v8       | 24.7 ms                                                               | 26.2 ms: 1.06x slower                                                 |
| regex_effbot   | 3.54 ms                                                               | 3.87 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240811-linux-x86_64-python-253c6a0b2f88b3327b71-3.14.0a0-253c6a0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 105 ms                                                                | 104 ms: 1.01x faster                                                  |
| unpickle_pure_python | 216 us                                                                | 214 us: 1.01x faster                                                  |
| xml_etree_generate   | 86.6 ms                                                               | 85.9 ms: 1.01x faster                                                 |
| xml_etree_process    | 59.9 ms                                                               | 59.5 ms: 1.01x faster                                                 |
| pickle_pure_python   | 300 us                                                                | 305 us: 1.02x slower                                                  |
| json_loads           | 27.6 us                                                               | 28.2 us: 1.02x slower                                                 |
| tomli_loads          | 2.03 sec                                                              | 2.11 sec: 1.04x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240811-linux-x86_64-python-253c6a0b2f88b3327b71-3.14.0a0-253c6a0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.12 ms                                                               | 7.05 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240811-linux-x86_64-python-253c6a0b2f88b3327b71-3.14.0a0-253c6a0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.2 ms                                                               | 11.0 ms: 1.02x faster                                                 |
| django_template | 34.0 ms                                                               | 34.3 ms: 1.01x slower                                                 |
| genshi_text     | 23.1 ms                                                               | 23.8 ms: 1.03x slower                                                 |
| genshi_xml      | 50.8 ms                                                               | 52.8 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240811-linux-x86_64-python-253c6a0b2f88b3327b71-3.14.0a0-253c6a0 | bm-20240812-linux-x86_64-faster%2dcpython-fix_122821-3.14.0a0-87e2bf8 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines               | 23.6 ms                                                               | 22.5 ms: 1.05x faster                                                 |
| gc_traversal             | 3.63 ms                                                               | 3.54 ms: 1.03x faster                                                 |
| create_gc_cycles         | 1.75 ms                                                               | 1.71 ms: 1.02x faster                                                 |
| pathlib                  | 16.1 ms                                                               | 15.8 ms: 1.02x faster                                                 |
| mako                     | 11.2 ms                                                               | 11.0 ms: 1.02x faster                                                 |
| crypto_pyaes             | 74.0 ms                                                               | 72.9 ms: 1.02x faster                                                 |
| async_tree_none_tg       | 302 ms                                                                | 298 ms: 1.01x faster                                                  |
| hexiom                   | 6.18 ms                                                               | 6.10 ms: 1.01x faster                                                 |
| logging_silent           | 100 ns                                                                | 99.2 ns: 1.01x faster                                                 |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site   | 7.12 ms                                                               | 7.05 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 105 ms                                                                | 104 ms: 1.01x faster                                                  |
| scimark_sor              | 126 ms                                                                | 125 ms: 1.01x faster                                                  |
| unpickle_pure_python     | 216 us                                                                | 214 us: 1.01x faster                                                  |
| xml_etree_generate       | 86.6 ms                                                               | 85.9 ms: 1.01x faster                                                 |
| xml_etree_process        | 59.9 ms                                                               | 59.5 ms: 1.01x faster                                                 |
| nbody                    | 88.2 ms                                                               | 87.7 ms: 1.01x faster                                                 |
| bpe_tokeniser            | 4.88 sec                                                              | 4.85 sec: 1.01x faster                                                |
| float                    | 79.3 ms                                                               | 78.9 ms: 1.01x faster                                                 |
| html5lib                 | 65.2 ms                                                               | 65.0 ms: 1.00x faster                                                 |
| generators               | 28.1 ms                                                               | 28.0 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                |
| pidigits                 | 187 ms                                                                | 188 ms: 1.00x slower                                                  |
| raytrace                 | 257 ms                                                                | 258 ms: 1.00x slower                                                  |
| nqueens                  | 79.2 ms                                                               | 79.7 ms: 1.01x slower                                                 |
| thrift                   | 782 us                                                                | 787 us: 1.01x slower                                                  |
| bench_thread_pool        | 786 us                                                                | 791 us: 1.01x slower                                                  |
| docutils                 | 2.71 sec                                                              | 2.73 sec: 1.01x slower                                                |
| meteor_contest           | 106 ms                                                                | 107 ms: 1.01x slower                                                  |
| asyncio_tcp              | 488 ms                                                                | 492 ms: 1.01x slower                                                  |
| django_template          | 34.0 ms                                                               | 34.3 ms: 1.01x slower                                                 |
| tornado_http             | 90.0 ms                                                               | 90.8 ms: 1.01x slower                                                 |
| scimark_monte_carlo      | 67.7 ms                                                               | 68.3 ms: 1.01x slower                                                 |
| sympy_integrate          | 19.6 ms                                                               | 19.8 ms: 1.01x slower                                                 |
| sqlglot_transpile        | 1.57 ms                                                               | 1.59 ms: 1.01x slower                                                 |
| chaos                    | 58.2 ms                                                               | 58.8 ms: 1.01x slower                                                 |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                 |
| sqlglot_optimize         | 53.3 ms                                                               | 53.8 ms: 1.01x slower                                                 |
| scimark_fft              | 363 ms                                                                | 367 ms: 1.01x slower                                                  |
| sqlglot_normalize        | 107 ms                                                                | 108 ms: 1.01x slower                                                  |
| telco                    | 8.17 ms                                                               | 8.26 ms: 1.01x slower                                                 |
| logging_format           | 6.18 us                                                               | 6.26 us: 1.01x slower                                                 |
| typing_runtime_protocols | 162 us                                                                | 164 us: 1.01x slower                                                  |
| logging_simple           | 5.53 us                                                               | 5.60 us: 1.01x slower                                                 |
| deepcopy_memo            | 29.7 us                                                               | 30.1 us: 1.01x slower                                                 |
| regex_compile            | 130 ms                                                                | 132 ms: 1.01x slower                                                  |
| comprehensions           | 16.6 us                                                               | 16.8 us: 1.01x slower                                                 |
| richards_super           | 51.6 ms                                                               | 52.3 ms: 1.01x slower                                                 |
| async_generators         | 437 ms                                                                | 443 ms: 1.01x slower                                                  |
| richards                 | 45.7 ms                                                               | 46.4 ms: 1.02x slower                                                 |
| pyflate                  | 471 ms                                                                | 478 ms: 1.02x slower                                                  |
| go                       | 139 ms                                                                | 141 ms: 1.02x slower                                                  |
| pprint_safe_repr         | 739 ms                                                                | 751 ms: 1.02x slower                                                  |
| pickle_pure_python       | 300 us                                                                | 305 us: 1.02x slower                                                  |
| spectral_norm            | 113 ms                                                                | 115 ms: 1.02x slower                                                  |
| json_loads               | 27.6 us                                                               | 28.2 us: 1.02x slower                                                 |
| regex_dna                | 222 ms                                                                | 227 ms: 1.02x slower                                                  |
| deepcopy                 | 260 us                                                                | 266 us: 1.02x slower                                                  |
| pprint_pformat           | 1.51 sec                                                              | 1.55 sec: 1.03x slower                                                |
| genshi_text              | 23.1 ms                                                               | 23.8 ms: 1.03x slower                                                 |
| deltablue                | 3.18 ms                                                               | 3.28 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult  | 4.61 ms                                                               | 4.76 ms: 1.03x slower                                                 |
| genshi_xml               | 50.8 ms                                                               | 52.8 ms: 1.04x slower                                                 |
| tomli_loads              | 2.03 sec                                                              | 2.11 sec: 1.04x slower                                                |
| deepcopy_reduce          | 2.67 us                                                               | 2.77 us: 1.04x slower                                                 |
| regex_v8                 | 24.7 ms                                                               | 26.2 ms: 1.06x slower                                                 |
| coverage                 | 84.3 ms                                                               | 90.8 ms: 1.08x slower                                                 |
| regex_effbot             | 3.54 ms                                                               | 3.87 ms: 1.09x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (21): async_tree_io_tg, async_tree_io, async_tree_memoization_tg, json, async_tree_cpu_io_mixed_tg, xml_etree_parse, async_tree_cpu_io_mixed, fannkuch, async_tree_none, sympy_expand, json_dumps, bench_mp_pool, pylint, sympy_str, 2to3, mdp, asyncio_websockets, sympy_sum, scimark_lu, pycparser, async_tree_memoization

# HPT report

- Reliability score: 99.17% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x