# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.01x slower
- HPT reliability: 80.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 3.22 sec                                                                    | 3.19 sec: 1.01x faster                                               |
| html5lib       | 70.5 ms                                                                     | 73.1 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                         |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io          | 820 ms                                                                      | 804 ms: 1.02x faster                                                 |
| coroutines             | 21.4 ms                                                                     | 21.2 ms: 1.01x faster                                                |
| async_generators       | 385 ms                                                                      | 383 ms: 1.00x faster                                                 |
| async_tree_memoization | 402 ms                                                                      | 406 ms: 1.01x slower                                                 |
| async_tree_io_tg       | 777 ms                                                                      | 792 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                         |

Benchmark hidden because not significant (8): asyncio_websockets, async_tree_memoization_tg, asyncio_tcp_ssl, asyncio_tcp, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 251 ms                                                                      | 250 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                         |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 25.8 ms                                                                     | 24.7 ms: 1.05x faster                                                |
| regex_effbot   | 3.52 ms                                                                     | 3.43 ms: 1.02x faster                                                |
| regex_dna      | 249 ms                                                                      | 245 ms: 1.01x faster                                                 |
| regex_compile  | 153 ms                                                                      | 152 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 148 ms                                                                      | 140 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                                      | 98.4 ms: 1.03x faster                                                |
| unpickle_pure_python | 220 us                                                                      | 215 us: 1.02x faster                                                 |
| xml_etree_generate   | 79.1 ms                                                                     | 78.0 ms: 1.01x faster                                                |
| pickle_list          | 4.24 us                                                                     | 4.20 us: 1.01x faster                                                |
| xml_etree_process    | 56.7 ms                                                                     | 56.2 ms: 1.01x faster                                                |
| json_dumps           | 10.5 ms                                                                     | 10.5 ms: 1.01x faster                                                |
| pickle               | 10.2 us                                                                     | 10.3 us: 1.01x slower                                                |
| pickle_pure_python   | 324 us                                                                      | 329 us: 1.01x slower                                                 |
| unpickle_list        | 4.60 us                                                                     | 4.76 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                         |

Benchmark hidden because not significant (4): json_loads, pickle_dict, tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 13.5 ms                                                                     | 13.4 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text    | 29.7 ms                                                                     | 29.0 ms: 1.02x faster                                                |
| genshi_xml     | 64.9 ms                                                                     | 64.4 ms: 1.01x faster                                                |
| mako           | 9.16 ms                                                                     | 9.20 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|--------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal             | 4.62 ms                                                                     | 4.30 ms: 1.08x faster                                                |
| xml_etree_parse          | 148 ms                                                                      | 140 ms: 1.06x faster                                                 |
| regex_v8                 | 25.8 ms                                                                     | 24.7 ms: 1.05x faster                                                |
| coverage                 | 84.0 ms                                                                     | 80.7 ms: 1.04x faster                                                |
| xml_etree_iterparse      | 101 ms                                                                      | 98.4 ms: 1.03x faster                                                |
| regex_effbot             | 3.52 ms                                                                     | 3.43 ms: 1.02x faster                                                |
| genshi_text              | 29.7 ms                                                                     | 29.0 ms: 1.02x faster                                                |
| unpickle_pure_python     | 220 us                                                                      | 215 us: 1.02x faster                                                 |
| pprint_pformat           | 1.61 sec                                                                    | 1.58 sec: 1.02x faster                                               |
| async_tree_io            | 820 ms                                                                      | 804 ms: 1.02x faster                                                 |
| scimark_lu               | 98.7 ms                                                                     | 96.9 ms: 1.02x faster                                                |
| pprint_safe_repr         | 768 ms                                                                      | 755 ms: 1.02x faster                                                 |
| richards_super           | 51.5 ms                                                                     | 50.6 ms: 1.02x faster                                                |
| regex_dna                | 249 ms                                                                      | 245 ms: 1.01x faster                                                 |
| xml_etree_generate       | 79.1 ms                                                                     | 78.0 ms: 1.01x faster                                                |
| bpe_tokeniser            | 4.76 sec                                                                    | 4.70 sec: 1.01x faster                                               |
| pickle_list              | 4.24 us                                                                     | 4.20 us: 1.01x faster                                                |
| coroutines               | 21.4 ms                                                                     | 21.2 ms: 1.01x faster                                                |
| sqlglot_optimize         | 69.4 ms                                                                     | 68.7 ms: 1.01x faster                                                |
| docutils                 | 3.22 sec                                                                    | 3.19 sec: 1.01x faster                                               |
| xml_etree_process        | 56.7 ms                                                                     | 56.2 ms: 1.01x faster                                                |
| genshi_xml               | 64.9 ms                                                                     | 64.4 ms: 1.01x faster                                                |
| sympy_expand             | 529 ms                                                                      | 525 ms: 1.01x faster                                                 |
| meteor_contest           | 134 ms                                                                      | 133 ms: 1.01x faster                                                 |
| python_startup           | 13.5 ms                                                                     | 13.4 ms: 1.01x faster                                                |
| json_dumps               | 10.5 ms                                                                     | 10.5 ms: 1.01x faster                                                |
| hexiom                   | 7.09 ms                                                                     | 7.06 ms: 1.00x faster                                                |
| dulwich_log              | 64.3 ms                                                                     | 64.0 ms: 1.00x faster                                                |
| sympy_str                | 319 ms                                                                      | 318 ms: 1.00x faster                                                 |
| create_gc_cycles         | 1.87 ms                                                                     | 1.87 ms: 1.00x faster                                                |
| async_generators         | 385 ms                                                                      | 383 ms: 1.00x faster                                                 |
| richards                 | 44.3 ms                                                                     | 44.2 ms: 1.00x faster                                                |
| regex_compile            | 153 ms                                                                      | 152 ms: 1.00x faster                                                 |
| pidigits                 | 251 ms                                                                      | 250 ms: 1.00x faster                                                 |
| pathlib                  | 15.7 ms                                                                     | 15.8 ms: 1.00x slower                                                |
| scimark_sparse_mat_mult  | 4.13 ms                                                                     | 4.14 ms: 1.00x slower                                                |
| mako                     | 9.16 ms                                                                     | 9.20 ms: 1.00x slower                                                |
| chaos                    | 66.4 ms                                                                     | 66.8 ms: 1.01x slower                                                |
| sqlglot_transpile        | 1.97 ms                                                                     | 1.98 ms: 1.01x slower                                                |
| telco                    | 7.65 ms                                                                     | 7.71 ms: 1.01x slower                                                |
| unpack_sequence          | 88.0 ns                                                                     | 88.7 ns: 1.01x slower                                                |
| crypto_pyaes             | 70.2 ms                                                                     | 70.7 ms: 1.01x slower                                                |
| spectral_norm            | 82.6 ms                                                                     | 83.3 ms: 1.01x slower                                                |
| pickle                   | 10.2 us                                                                     | 10.3 us: 1.01x slower                                                |
| async_tree_memoization   | 402 ms                                                                      | 406 ms: 1.01x slower                                                 |
| nqueens                  | 99.7 ms                                                                     | 101 ms: 1.01x slower                                                 |
| deepcopy_memo            | 27.4 us                                                                     | 27.7 us: 1.01x slower                                                |
| logging_simple           | 6.53 us                                                                     | 6.61 us: 1.01x slower                                                |
| thrift                   | 905 us                                                                      | 916 us: 1.01x slower                                                 |
| pycparser                | 1.28 sec                                                                    | 1.29 sec: 1.01x slower                                               |
| pickle_pure_python       | 324 us                                                                      | 329 us: 1.01x slower                                                 |
| logging_silent           | 97.5 ns                                                                     | 98.9 ns: 1.02x slower                                                |
| scimark_fft              | 278 ms                                                                      | 283 ms: 1.02x slower                                                 |
| deepcopy                 | 294 us                                                                      | 299 us: 1.02x slower                                                 |
| async_tree_io_tg         | 777 ms                                                                      | 792 ms: 1.02x slower                                                 |
| generators               | 38.8 ms                                                                     | 39.5 ms: 1.02x slower                                                |
| scimark_sor              | 104 ms                                                                      | 107 ms: 1.03x slower                                                 |
| raytrace                 | 312 ms                                                                      | 322 ms: 1.03x slower                                                 |
| unpickle_list            | 4.60 us                                                                     | 4.76 us: 1.03x slower                                                |
| html5lib                 | 70.5 ms                                                                     | 73.1 ms: 1.04x slower                                                |
| typing_runtime_protocols | 181 us                                                                      | 189 us: 1.04x slower                                                 |
| bench_mp_pool            | 1.57 sec                                                                    | 4.58 sec: 2.91x slower                                               |
| Geometric mean           | (ref)                                                                       | 1.01x slower                                                         |

Benchmark hidden because not significant (35): json_loads, pylint, bench_thread_pool, pickle_dict, asyncio_websockets, json, deepcopy_reduce, comprehensions, sqlite_synth, sympy_integrate, scimark_monte_carlo, tomli_loads, python_startup_no_site, sqlglot_normalize, sqlglot_parse, sympy_sum, deltablue, go, nbody, mdp, pyflate, async_tree_memoization_tg, 2to3, asyncio_tcp_ssl, tornado_http, logging_format, float, fannkuch, asyncio_tcp, unpickle, async_tree_none_tg, async_tree_cpu_io_mixed_tg, django_template, async_tree_cpu_io_mixed, async_tree_none

# HPT report

- Reliability score: 80.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x