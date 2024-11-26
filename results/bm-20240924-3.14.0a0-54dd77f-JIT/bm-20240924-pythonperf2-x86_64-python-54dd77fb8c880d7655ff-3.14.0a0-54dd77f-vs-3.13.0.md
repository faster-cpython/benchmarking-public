# Results vs. 3.13.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: linux-x86_64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.020x faster
- HPT reliability: 93.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 312 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.4 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                       | 122 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 394 ms: 1.16x faster                                                        |
| async_tree_none            | 370 ms                                                       | 325 ms: 1.14x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 408 ms: 1.10x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 313 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 795 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 806 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 578 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| async_generators           | 364 ms                                                       | 387 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 73.6 ms: 1.11x faster                                                       |
| nbody          | 92.1 ms                                                      | 83.8 ms: 1.10x faster                                                       |
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.50 ms: 1.00x faster                                                       |
| regex_v8       | 24.9 ms                                                      | 25.8 ms: 1.04x slower                                                       |
| regex_compile  | 143 ms                                                       | 148 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|---------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads         | 2.43 sec                                                     | 2.11 sec: 1.15x faster                                                      |
| xml_etree_process   | 60.7 ms                                                      | 56.4 ms: 1.08x faster                                                       |
| xml_etree_generate  | 85.2 ms                                                      | 80.2 ms: 1.06x faster                                                       |
| json_loads          | 24.7 us                                                      | 24.2 us: 1.02x faster                                                       |
| json_dumps          | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                                       |
| xml_etree_iterparse | 99.8 ms                                                      | 98.2 ms: 1.02x faster                                                       |
| pickle_pure_python  | 322 us                                                       | 325 us: 1.01x slower                                                        |
| Geometric mean      | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.00 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.16 ms: 1.13x faster                                                       |
| genshi_text     | 27.2 ms                                                      | 29.5 ms: 1.08x slower                                                       |
| django_template | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                       |
| genshi_xml      | 58.0 ms                                                      | 68.6 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 26.9 us: 1.45x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 1.91 ms: 1.39x faster                                                       |
| deepcopy                   | 388 us                                                       | 298 us: 1.30x faster                                                        |
| scimark_sor                | 125 ms                                                       | 104 ms: 1.20x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 2.92 us: 1.19x faster                                                       |
| richards                   | 52.5 ms                                                      | 44.6 ms: 1.18x faster                                                       |
| richards_super             | 60.2 ms                                                      | 51.6 ms: 1.17x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 394 ms: 1.16x faster                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.11 sec: 1.15x faster                                                      |
| async_tree_none            | 370 ms                                                       | 325 ms: 1.14x faster                                                        |
| mako                       | 10.3 ms                                                      | 9.16 ms: 1.13x faster                                                       |
| go                         | 167 ms                                                       | 148 ms: 1.13x faster                                                        |
| float                      | 81.6 ms                                                      | 73.6 ms: 1.11x faster                                                       |
| pyflate                    | 493 ms                                                       | 445 ms: 1.11x faster                                                        |
| nbody                      | 92.1 ms                                                      | 83.8 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 408 ms: 1.10x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 313 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 56.4 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.73 sec: 1.08x faster                                                      |
| telco                      | 8.77 ms                                                      | 8.20 ms: 1.07x faster                                                       |
| fannkuch                   | 384 ms                                                       | 360 ms: 1.07x faster                                                        |
| deltablue                  | 3.38 ms                                                      | 3.17 ms: 1.07x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 80.2 ms: 1.06x faster                                                       |
| coverage                   | 84.5 ms                                                      | 79.8 ms: 1.06x faster                                                       |
| json                       | 5.62 ms                                                      | 5.33 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 792 ms: 1.05x faster                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 69.9 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.01 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                        |
| scimark_fft                | 298 ms                                                       | 287 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 795 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 806 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 578 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                      |
| json_loads                 | 24.7 us                                                      | 24.2 us: 1.02x faster                                                       |
| json_dumps                 | 10.8 ms                                                      | 10.6 ms: 1.02x faster                                                       |
| html5lib                   | 72.9 ms                                                      | 71.4 ms: 1.02x faster                                                       |
| regex_dna                  | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 64.3 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 98.2 ms: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| gc_traversal               | 4.48 ms                                                      | 4.42 ms: 1.01x faster                                                       |
| meteor_contest             | 130 ms                                                       | 129 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.50 ms: 1.00x faster                                                       |
| python_startup_no_site     | 8.93 ms                                                      | 9.00 ms: 1.01x slower                                                       |
| pycparser                  | 1.28 sec                                                     | 1.29 sec: 1.01x slower                                                      |
| pickle_pure_python         | 322 us                                                       | 325 us: 1.01x slower                                                        |
| scimark_lu                 | 97.4 ms                                                      | 98.4 ms: 1.01x slower                                                       |
| mdp                        | 2.53 sec                                                     | 2.60 sec: 1.03x slower                                                      |
| tornado_http               | 119 ms                                                       | 122 ms: 1.03x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 25.8 ms: 1.04x slower                                                       |
| regex_compile              | 143 ms                                                       | 148 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 183 us: 1.04x slower                                                        |
| logging_format             | 6.95 us                                                      | 7.26 us: 1.04x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.5 ms: 1.05x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.2 us: 1.05x slower                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 5.08 ms: 1.05x slower                                                       |
| sympy_str                  | 297 ms                                                       | 313 ms: 1.05x slower                                                        |
| sympy_expand               | 506 ms                                                       | 537 ms: 1.06x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.67 us: 1.06x slower                                                       |
| async_generators           | 364 ms                                                       | 387 ms: 1.06x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 98.2 ms: 1.06x slower                                                       |
| 2to3                       | 293 ms                                                       | 312 ms: 1.06x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 104 ns: 1.07x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 6.95 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 128 ms: 1.08x slower                                                        |
| genshi_text                | 27.2 ms                                                      | 29.5 ms: 1.08x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.49 ms: 1.09x slower                                                       |
| django_template            | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                       |
| generators                 | 33.9 ms                                                      | 37.3 ms: 1.10x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 170 ms: 1.10x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.95 ms: 1.10x slower                                                       |
| chaos                      | 60.6 ms                                                      | 66.9 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 65.6 ms: 1.12x slower                                                       |
| sympy_integrate            | 23.4 ms                                                      | 26.5 ms: 1.13x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.18 sec: 1.13x slower                                                      |
| genshi_xml                 | 58.0 ms                                                      | 68.6 ms: 1.18x slower                                                       |
| pylint                     | 345 ms                                                       | 411 ms: 1.19x slower                                                        |
| raytrace                   | 267 ms                                                       | 332 ms: 1.24x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (5): asyncio_websockets, thrift, bench_thread_pool, xml_etree_parse, unpickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 93.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x