# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.004x slower
- HPT reliability: 51.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 314 ms: 1.07x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                      |
| html5lib       | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                       |
| sphinx         | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                      |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 377 ms: 1.22x faster                                                        |
| async_tree_none            | 370 ms                                                       | 332 ms: 1.11x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 321 ms: 1.06x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 577 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| async_tree_io_tg           | 823 ms                                                       | 863 ms: 1.05x slower                                                        |
| async_generators           | 364 ms                                                       | 388 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 83.3 ms: 1.10x faster                                                       |
| float          | 81.6 ms                                                      | 79.3 ms: 1.03x faster                                                       |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 247 ms: 1.04x slower                                                        |
| regex_compile  | 143 ms                                                       | 152 ms: 1.07x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 26.9 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.15 sec: 1.13x faster                                                      |
| xml_etree_generate   | 85.2 ms                                                      | 82.0 ms: 1.04x faster                                                       |
| xml_etree_process    | 60.7 ms                                                      | 58.6 ms: 1.04x faster                                                       |
| json_loads           | 24.7 us                                                      | 24.3 us: 1.02x faster                                                       |
| json_dumps           | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                       |
| pickle_pure_python   | 322 us                                                       | 337 us: 1.05x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 226 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.39 ms: 1.10x faster                                                       |
| genshi_text     | 27.2 ms                                                      | 28.3 ms: 1.04x slower                                                       |
| genshi_xml      | 58.0 ms                                                      | 65.1 ms: 1.12x slower                                                       |
| django_template | 38.9 ms                                                      | 43.9 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 29.9 us: 1.30x faster                                                       |
| deepcopy                   | 388 us                                                       | 313 us: 1.24x faster                                                        |
| richards_super             | 60.2 ms                                                      | 48.9 ms: 1.23x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 377 ms: 1.22x faster                                                        |
| scimark_sor                | 125 ms                                                       | 103 ms: 1.21x faster                                                        |
| richards                   | 52.5 ms                                                      | 43.7 ms: 1.20x faster                                                       |
| telco                      | 8.77 ms                                                      | 7.73 ms: 1.13x faster                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.15 sec: 1.13x faster                                                      |
| deepcopy_reduce            | 3.49 us                                                      | 3.11 us: 1.12x faster                                                       |
| async_tree_none            | 370 ms                                                       | 332 ms: 1.11x faster                                                        |
| nbody                      | 92.1 ms                                                      | 83.3 ms: 1.10x faster                                                       |
| go                         | 167 ms                                                       | 151 ms: 1.10x faster                                                        |
| json                       | 5.62 ms                                                      | 5.10 ms: 1.10x faster                                                       |
| mako                       | 10.3 ms                                                      | 9.39 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.09x faster                                                        |
| logging_silent             | 97.5 ns                                                      | 90.8 ns: 1.07x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.77 sec: 1.07x faster                                                      |
| async_tree_none_tg         | 342 ms                                                       | 321 ms: 1.06x faster                                                        |
| fannkuch                   | 384 ms                                                       | 364 ms: 1.06x faster                                                        |
| pyflate                    | 493 ms                                                       | 467 ms: 1.06x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 92.8 ms: 1.05x faster                                                       |
| python_startup             | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 82.0 ms: 1.04x faster                                                       |
| scimark_lu                 | 97.4 ms                                                      | 93.9 ms: 1.04x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 58.6 ms: 1.04x faster                                                       |
| asyncio_websockets         | 395 ms                                                       | 381 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 807 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 577 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                      |
| html5lib                   | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                       |
| float                      | 81.6 ms                                                      | 79.3 ms: 1.03x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 71.5 ms: 1.03x faster                                                       |
| scimark_fft                | 298 ms                                                       | 291 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.02x faster                                                        |
| deltablue                  | 3.38 ms                                                      | 3.31 ms: 1.02x faster                                                       |
| thrift                     | 918 us                                                       | 899 us: 1.02x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 64.4 ms: 1.02x faster                                                       |
| json_loads                 | 24.7 us                                                      | 24.3 us: 1.02x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.27 sec: 1.01x faster                                                      |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 8.98 ms: 1.01x slower                                                       |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.01x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 21.8 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 176 us                                                       | 178 us: 1.02x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 952 us: 1.02x slower                                                        |
| logging_format             | 6.95 us                                                      | 7.14 us: 1.03x slower                                                       |
| mdp                        | 2.53 sec                                                     | 2.60 sec: 1.03x slower                                                      |
| tornado_http               | 119 ms                                                       | 123 ms: 1.03x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                       |
| regex_dna                  | 238 ms                                                       | 247 ms: 1.04x slower                                                        |
| genshi_text                | 27.2 ms                                                      | 28.3 ms: 1.04x slower                                                       |
| pickle_pure_python         | 322 us                                                       | 337 us: 1.05x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 226 us: 1.05x slower                                                        |
| async_tree_io_tg           | 823 ms                                                       | 863 ms: 1.05x slower                                                        |
| sympy_expand               | 506 ms                                                       | 534 ms: 1.05x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.63 us: 1.06x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.47 ms: 1.06x slower                                                       |
| regex_compile              | 143 ms                                                       | 152 ms: 1.07x slower                                                        |
| async_generators           | 364 ms                                                       | 388 ms: 1.07x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.6 ms: 1.07x slower                                                       |
| 2to3                       | 293 ms                                                       | 314 ms: 1.07x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 26.9 ms: 1.08x slower                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 2.89 ms: 1.09x slower                                                       |
| sympy_str                  | 297 ms                                                       | 324 ms: 1.09x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.9 us: 1.09x slower                                                       |
| chaos                      | 60.6 ms                                                      | 67.0 ms: 1.11x slower                                                       |
| hexiom                     | 6.47 ms                                                      | 7.16 ms: 1.11x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.52 ms: 1.11x slower                                                       |
| nqueens                    | 92.3 ms                                                      | 103 ms: 1.12x slower                                                        |
| genshi_xml                 | 58.0 ms                                                      | 65.1 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 134 ms: 1.13x slower                                                        |
| django_template            | 38.9 ms                                                      | 43.9 ms: 1.13x slower                                                       |
| generators                 | 33.9 ms                                                      | 38.3 ms: 1.13x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| sphinx                     | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                      |
| docutils                   | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                      |
| sympy_sum                  | 154 ms                                                       | 176 ms: 1.15x slower                                                        |
| raytrace                   | 267 ms                                                       | 307 ms: 1.15x slower                                                        |
| gc_traversal               | 4.48 ms                                                      | 5.21 ms: 1.16x slower                                                       |
| sympy_integrate            | 23.4 ms                                                      | 27.6 ms: 1.18x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 70.3 ms: 1.20x slower                                                       |
| pylint                     | 345 ms                                                       | 422 ms: 1.22x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 3.16 sec: 656.29x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (5): coverage, regex_effbot, xml_etree_parse, xml_etree_iterparse, async_tree_io
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.004x slower
# HPT report

- Reliability score: 51.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x