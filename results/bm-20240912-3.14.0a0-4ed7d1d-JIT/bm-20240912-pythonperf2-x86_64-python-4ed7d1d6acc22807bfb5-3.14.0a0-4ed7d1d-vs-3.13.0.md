# Results vs. 3.13.0

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.020x faster
- HPT reliability: 93.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 309 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.15 sec: 1.12x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.1 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                       | 122 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 393 ms: 1.17x faster                                                        |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 404 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 311 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 576 ms: 1.03x faster                                                        |
| async_tree_io              | 832 ms                                                       | 812 ms: 1.02x faster                                                        |
| async_generators           | 364 ms                                                       | 393 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (3): coroutines, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 81.8 ms: 1.13x faster                                                       |
| float          | 81.6 ms                                                      | 74.6 ms: 1.09x faster                                                       |
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 233 ms: 1.03x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.49 ms: 1.01x faster                                                       |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 25.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.13 sec: 1.14x faster                                                      |
| xml_etree_process    | 60.7 ms                                                      | 55.9 ms: 1.09x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 80.1 ms: 1.06x faster                                                       |
| json_loads           | 24.7 us                                                      | 23.9 us: 1.03x faster                                                       |
| json_dumps           | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 98.9 ms: 1.01x faster                                                       |
| pickle_pure_python   | 322 us                                                       | 326 us: 1.01x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.00 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.23 ms: 1.12x faster                                                       |
| genshi_text     | 27.2 ms                                                      | 29.5 ms: 1.09x slower                                                       |
| django_template | 38.9 ms                                                      | 42.8 ms: 1.10x slower                                                       |
| genshi_xml      | 58.0 ms                                                      | 66.0 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 27.1 us: 1.44x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 1.94 ms: 1.36x faster                                                       |
| deepcopy                   | 388 us                                                       | 289 us: 1.34x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.92 us: 1.20x faster                                                       |
| scimark_sor                | 125 ms                                                       | 105 ms: 1.20x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 81.6 ms: 1.19x faster                                                       |
| richards                   | 52.5 ms                                                      | 44.5 ms: 1.18x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 393 ms: 1.17x faster                                                        |
| richards_super             | 60.2 ms                                                      | 52.1 ms: 1.16x faster                                                       |
| async_tree_none            | 370 ms                                                       | 323 ms: 1.15x faster                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.13 sec: 1.14x faster                                                      |
| nbody                      | 92.1 ms                                                      | 81.8 ms: 1.13x faster                                                       |
| mako                       | 10.3 ms                                                      | 9.23 ms: 1.12x faster                                                       |
| go                         | 167 ms                                                       | 149 ms: 1.12x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 404 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 311 ms: 1.10x faster                                                        |
| pyflate                    | 493 ms                                                       | 449 ms: 1.10x faster                                                        |
| float                      | 81.6 ms                                                      | 74.6 ms: 1.09x faster                                                       |
| json                       | 5.62 ms                                                      | 5.14 ms: 1.09x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 55.9 ms: 1.09x faster                                                       |
| fannkuch                   | 384 ms                                                       | 358 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.75 sec: 1.07x faster                                                      |
| xml_etree_generate         | 85.2 ms                                                      | 80.1 ms: 1.06x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 69.3 ms: 1.06x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.28 ms: 1.06x faster                                                       |
| deltablue                  | 3.38 ms                                                      | 3.21 ms: 1.06x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 796 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 549 ms: 1.05x faster                                                        |
| coverage                   | 84.5 ms                                                      | 81.3 ms: 1.04x faster                                                       |
| thrift                     | 918 us                                                       | 885 us: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 576 ms: 1.03x faster                                                        |
| json_loads                 | 24.7 us                                                      | 23.9 us: 1.03x faster                                                       |
| pprint_pformat             | 1.70 sec                                                     | 1.66 sec: 1.03x faster                                                      |
| scimark_fft                | 298 ms                                                       | 290 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.10 ms: 1.03x faster                                                       |
| regex_dna                  | 238 ms                                                       | 233 ms: 1.03x faster                                                        |
| pycparser                  | 1.28 sec                                                     | 1.25 sec: 1.02x faster                                                      |
| html5lib                   | 72.9 ms                                                      | 71.1 ms: 1.02x faster                                                       |
| async_tree_io              | 832 ms                                                       | 812 ms: 1.02x faster                                                        |
| json_dumps                 | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                                       |
| dulwich_log                | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 98.9 ms: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.49 ms: 1.01x faster                                                       |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.00x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 9.00 ms: 1.01x slower                                                       |
| pickle_pure_python         | 322 us                                                       | 326 us: 1.01x slower                                                        |
| mdp                        | 2.53 sec                                                     | 2.57 sec: 1.02x slower                                                      |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                                        |
| scimark_lu                 | 97.4 ms                                                      | 99.3 ms: 1.02x slower                                                       |
| tornado_http               | 119 ms                                                       | 122 ms: 1.03x slower                                                        |
| logging_format             | 6.95 us                                                      | 7.15 us: 1.03x slower                                                       |
| typing_runtime_protocols   | 176 us                                                       | 181 us: 1.03x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 100 ns: 1.03x slower                                                        |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 25.7 ms: 1.03x slower                                                       |
| sympy_expand               | 506 ms                                                       | 533 ms: 1.05x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.2 us: 1.05x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.62 us: 1.06x slower                                                       |
| 2to3                       | 293 ms                                                       | 309 ms: 1.06x slower                                                        |
| sympy_str                  | 297 ms                                                       | 313 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.9 ms: 1.06x slower                                                       |
| nqueens                    | 92.3 ms                                                      | 99.1 ms: 1.07x slower                                                       |
| hexiom                     | 6.47 ms                                                      | 6.98 ms: 1.08x slower                                                       |
| async_generators           | 364 ms                                                       | 393 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 129 ms: 1.08x slower                                                        |
| chaos                      | 60.6 ms                                                      | 65.7 ms: 1.08x slower                                                       |
| genshi_text                | 27.2 ms                                                      | 29.5 ms: 1.09x slower                                                       |
| gc_traversal               | 4.48 ms                                                      | 4.87 ms: 1.09x slower                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 5.25 ms: 1.09x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.49 ms: 1.09x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 169 ms: 1.10x slower                                                        |
| django_template            | 38.9 ms                                                      | 42.8 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                       |
| generators                 | 33.9 ms                                                      | 37.6 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 65.7 ms: 1.12x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.15 sec: 1.12x slower                                                      |
| sympy_integrate            | 23.4 ms                                                      | 26.6 ms: 1.14x slower                                                       |
| genshi_xml                 | 58.0 ms                                                      | 66.0 ms: 1.14x slower                                                       |
| raytrace                   | 267 ms                                                       | 310 ms: 1.16x slower                                                        |
| pylint                     | 345 ms                                                       | 410 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (5): bench_thread_pool, xml_etree_parse, coroutines, asyncio_websockets, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240912-3.14.0a0-4ed7d1d-JIT/bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 93.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x