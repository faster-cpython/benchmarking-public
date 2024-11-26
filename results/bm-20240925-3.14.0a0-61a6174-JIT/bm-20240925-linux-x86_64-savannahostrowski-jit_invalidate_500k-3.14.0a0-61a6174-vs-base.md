# Results vs. base

- fork: savannahostrowski
- ref: jit_invalidate_500k
- machine: linux-x86_64
- commit hash: 61a6174
- commit date: 2024-09-25
- overall geometric mean: 1.007x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 273 ms                                                                | 276 ms: 1.01x slower                                                            |
| docutils       | 2.94 sec                                                              | 2.93 sec: 1.00x faster                                                          |
| html5lib       | 64.5 ms                                                               | 62.0 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (13): coroutines, asyncio_tcp_ssl, async_generators, async_tree_memoization_tg, asyncio_tcp, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                                            |
| float          | 69.5 ms                                                               | 69.8 ms: 1.00x slower                                                           |
| nbody          | 79.6 ms                                                               | 81.4 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                | 212 ms: 1.07x faster                                                            |
| regex_v8       | 24.7 ms                                                               | 24.8 ms: 1.00x slower                                                           |
| regex_effbot   | 3.70 ms                                                               | 3.70 ms: 1.00x slower                                                           |
| regex_compile  | 142 ms                                                                | 142 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 10.0 ms                                                               | 9.81 ms: 1.02x faster                                                           |
| pickle_pure_python   | 308 us                                                                | 303 us: 1.02x faster                                                            |
| pickle_list          | 5.18 us                                                               | 5.11 us: 1.01x faster                                                           |
| pickle               | 11.8 us                                                               | 11.7 us: 1.01x faster                                                           |
| pickle_dict          | 35.0 us                                                               | 35.0 us: 1.00x faster                                                           |
| xml_etree_iterparse  | 98.1 ms                                                               | 98.7 ms: 1.01x slower                                                           |
| json_loads           | 26.9 us                                                               | 27.2 us: 1.01x slower                                                           |
| unpickle_pure_python | 214 us                                                                | 216 us: 1.01x slower                                                            |
| unpickle_list        | 5.19 us                                                               | 5.27 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (5): unpickle, xml_etree_parse, xml_etree_generate, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                               | 7.06 ms: 1.00x slower                                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                               | 9.74 ms: 1.02x faster                                                           |
| django_template | 35.6 ms                                                               | 36.0 ms: 1.01x slower                                                           |
| genshi_text     | 24.4 ms                                                               | 24.8 ms: 1.02x slower                                                           |
| genshi_xml      | 56.5 ms                                                               | 58.3 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20240924-linux-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna                | 225 ms                                                                | 212 ms: 1.07x faster                                                            |
| html5lib                 | 64.5 ms                                                               | 62.0 ms: 1.04x faster                                                           |
| gc_traversal             | 3.90 ms                                                               | 3.77 ms: 1.03x faster                                                           |
| json_dumps               | 10.0 ms                                                               | 9.81 ms: 1.02x faster                                                           |
| mako                     | 9.96 ms                                                               | 9.74 ms: 1.02x faster                                                           |
| pycparser                | 1.20 sec                                                              | 1.18 sec: 1.02x faster                                                          |
| mdp                      | 2.59 sec                                                              | 2.54 sec: 1.02x faster                                                          |
| pyflate                  | 447 ms                                                                | 439 ms: 1.02x faster                                                            |
| pickle_pure_python       | 308 us                                                                | 303 us: 1.02x faster                                                            |
| pickle_list              | 5.18 us                                                               | 5.11 us: 1.01x faster                                                           |
| pickle                   | 11.8 us                                                               | 11.7 us: 1.01x faster                                                           |
| fannkuch                 | 380 ms                                                                | 377 ms: 1.01x faster                                                            |
| create_gc_cycles         | 1.76 ms                                                               | 1.75 ms: 1.01x faster                                                           |
| logging_silent           | 104 ns                                                                | 103 ns: 1.00x faster                                                            |
| docutils                 | 2.94 sec                                                              | 2.93 sec: 1.00x faster                                                          |
| pickle_dict              | 35.0 us                                                               | 35.0 us: 1.00x faster                                                           |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x faster                                                            |
| regex_v8                 | 24.7 ms                                                               | 24.8 ms: 1.00x slower                                                           |
| regex_effbot             | 3.70 ms                                                               | 3.70 ms: 1.00x slower                                                           |
| regex_compile            | 142 ms                                                                | 142 ms: 1.00x slower                                                            |
| python_startup_no_site   | 7.04 ms                                                               | 7.06 ms: 1.00x slower                                                           |
| bpe_tokeniser            | 4.43 sec                                                              | 4.45 sec: 1.00x slower                                                          |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| sqlglot_transpile        | 1.68 ms                                                               | 1.69 ms: 1.00x slower                                                           |
| float                    | 69.5 ms                                                               | 69.8 ms: 1.00x slower                                                           |
| xml_etree_iterparse      | 98.1 ms                                                               | 98.7 ms: 1.01x slower                                                           |
| typing_runtime_protocols | 163 us                                                                | 164 us: 1.01x slower                                                            |
| pathlib                  | 15.8 ms                                                               | 15.9 ms: 1.01x slower                                                           |
| raytrace                 | 274 ms                                                                | 276 ms: 1.01x slower                                                            |
| json_loads               | 26.9 us                                                               | 27.2 us: 1.01x slower                                                           |
| 2to3                     | 273 ms                                                                | 276 ms: 1.01x slower                                                            |
| scimark_sor              | 116 ms                                                                | 117 ms: 1.01x slower                                                            |
| unpickle_pure_python     | 214 us                                                                | 216 us: 1.01x slower                                                            |
| django_template          | 35.6 ms                                                               | 36.0 ms: 1.01x slower                                                           |
| scimark_lu               | 110 ms                                                                | 111 ms: 1.01x slower                                                            |
| sympy_expand             | 500 ms                                                                | 506 ms: 1.01x slower                                                            |
| sympy_str                | 296 ms                                                                | 300 ms: 1.01x slower                                                            |
| dulwich_log              | 67.7 ms                                                               | 68.6 ms: 1.01x slower                                                           |
| deltablue                | 3.16 ms                                                               | 3.20 ms: 1.01x slower                                                           |
| sqlglot_optimize         | 57.6 ms                                                               | 58.4 ms: 1.01x slower                                                           |
| go                       | 131 ms                                                                | 133 ms: 1.01x slower                                                            |
| sympy_integrate          | 22.6 ms                                                               | 22.9 ms: 1.01x slower                                                           |
| unpickle_list            | 5.19 us                                                               | 5.27 us: 1.01x slower                                                           |
| bench_thread_pool        | 831 us                                                                | 844 us: 1.02x slower                                                            |
| hexiom                   | 6.86 ms                                                               | 6.97 ms: 1.02x slower                                                           |
| sqlite_synth             | 2.71 us                                                               | 2.75 us: 1.02x slower                                                           |
| sympy_sum                | 171 ms                                                                | 174 ms: 1.02x slower                                                            |
| json                     | 5.08 ms                                                               | 5.17 ms: 1.02x slower                                                           |
| deepcopy_reduce          | 2.62 us                                                               | 2.67 us: 1.02x slower                                                           |
| genshi_text              | 24.4 ms                                                               | 24.8 ms: 1.02x slower                                                           |
| scimark_fft              | 306 ms                                                                | 312 ms: 1.02x slower                                                            |
| deepcopy_memo            | 26.8 us                                                               | 27.4 us: 1.02x slower                                                           |
| nbody                    | 79.6 ms                                                               | 81.4 ms: 1.02x slower                                                           |
| meteor_contest           | 105 ms                                                                | 108 ms: 1.02x slower                                                            |
| unpack_sequence          | 109 ns                                                                | 112 ns: 1.02x slower                                                            |
| logging_format           | 6.01 us                                                               | 6.15 us: 1.02x slower                                                           |
| crypto_pyaes             | 65.8 ms                                                               | 67.5 ms: 1.03x slower                                                           |
| logging_simple           | 5.49 us                                                               | 5.65 us: 1.03x slower                                                           |
| genshi_xml               | 56.5 ms                                                               | 58.3 ms: 1.03x slower                                                           |
| richards                 | 39.8 ms                                                               | 41.1 ms: 1.03x slower                                                           |
| pprint_pformat           | 1.51 sec                                                              | 1.56 sec: 1.03x slower                                                          |
| richards_super           | 45.2 ms                                                               | 46.9 ms: 1.04x slower                                                           |
| comprehensions           | 16.4 us                                                               | 17.0 us: 1.04x slower                                                           |
| deepcopy                 | 255 us                                                                | 266 us: 1.04x slower                                                            |
| nqueens                  | 85.0 ms                                                               | 88.5 ms: 1.04x slower                                                           |
| scimark_sparse_mat_mult  | 4.23 ms                                                               | 4.40 ms: 1.04x slower                                                           |
| spectral_norm            | 98.8 ms                                                               | 104 ms: 1.05x slower                                                            |
| generators               | 33.0 ms                                                               | 34.9 ms: 1.06x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (29): unpickle, xml_etree_parse, xml_etree_generate, telco, xml_etree_process, coroutines, asyncio_tcp_ssl, async_generators, async_tree_memoization_tg, asyncio_tcp, coverage, sqlglot_normalize, tornado_http, bench_mp_pool, asyncio_websockets, sqlglot_parse, async_tree_cpu_io_mixed, tomli_loads, chaos, async_tree_none_tg, thrift, pprint_safe_repr, scimark_monte_carlo, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_none, pylint

- Geometric mean (including insignificant results): 1.007x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x