# Results vs. base

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.015x faster
- HPT reliability: 62.55%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 226 ms                                                                                                                 | 228 ms: 1.01x slower                                                                                                       |
| docutils       | 1.69 sec                                                                                                               | 1.75 sec: 1.04x slower                                                                                                     |
| sphinx         | 658 ms                                                                                                                 | 673 ms: 1.02x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 315 ms                                                                                                                 | 304 ms: 1.04x faster                                                                                                       |
| coroutines                 | 13.5 ms                                                                                                                | 13.6 ms: 1.01x slower                                                                                                      |
| asyncio_tcp_ssl            | 1.43 sec                                                                                                               | 1.45 sec: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 342 ms                                                                                                                 | 347 ms: 1.01x slower                                                                                                       |
| async_tree_cpu_io_mixed    | 342 ms                                                                                                                 | 348 ms: 1.02x slower                                                                                                       |
| async_tree_memoization     | 222 ms                                                                                                                 | 227 ms: 1.02x slower                                                                                                       |
| async_generators           | 234 ms                                                                                                                 | 250 ms: 1.07x slower                                                                                                       |
| Geometric mean             | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (6): asyncio_tcp, async_tree_io, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 71.7 ms                                                                                                                | 63.4 ms: 1.13x faster                                                                                                      |
| pidigits       | 148 ms                                                                                                                 | 149 ms: 1.01x slower                                                                                                       |
| float          | 46.1 ms                                                                                                                | 46.9 ms: 1.02x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                                                                                | 13.5 ms: 1.02x faster                                                                                                      |
| regex_compile  | 86.8 ms                                                                                                                | 86.2 ms: 1.01x faster                                                                                                      |
| regex_dna      | 114 ms                                                                                                                 | 116 ms: 1.02x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                                                                                 | 125 us: 1.21x faster                                                                                                       |
| tomli_loads          | 1.46 sec                                                                                                               | 1.24 sec: 1.18x faster                                                                                                     |
| xml_etree_generate   | 58.8 ms                                                                                                                | 52.6 ms: 1.12x faster                                                                                                      |
| xml_etree_process    | 41.6 ms                                                                                                                | 38.3 ms: 1.09x faster                                                                                                      |
| pickle_pure_python   | 227 us                                                                                                                 | 217 us: 1.05x faster                                                                                                       |
| pickle_list          | 3.51 us                                                                                                                | 3.37 us: 1.04x faster                                                                                                      |
| pickle_dict          | 20.6 us                                                                                                                | 19.8 us: 1.04x faster                                                                                                      |
| xml_etree_iterparse  | 64.2 ms                                                                                                                | 63.0 ms: 1.02x faster                                                                                                      |
| json_loads           | 15.1 us                                                                                                                | 15.3 us: 1.02x slower                                                                                                      |
| json_dumps           | 6.99 ms                                                                                                                | 7.13 ms: 1.02x slower                                                                                                      |
| pickle               | 8.03 us                                                                                                                | 8.31 us: 1.03x slower                                                                                                      |
| unpickle_list        | 2.79 us                                                                                                                | 2.91 us: 1.04x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 26.1 ms                                                                                                                | 25.7 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.84 ms                                                                                                                | 5.76 ms: 1.19x faster                                                                                                      |
| genshi_text    | 17.5 ms                                                                                                                | 17.3 ms: 1.01x faster                                                                                                      |
| genshi_xml     | 38.0 ms                                                                                                                | 40.1 ms: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json | results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 151 us                                                                                                                 | 125 us: 1.21x faster                                                                                                       |
| mako                       | 6.84 ms                                                                                                                | 5.76 ms: 1.19x faster                                                                                                      |
| tomli_loads                | 1.46 sec                                                                                                               | 1.24 sec: 1.18x faster                                                                                                     |
| scimark_fft                | 184 ms                                                                                                                 | 159 ms: 1.16x faster                                                                                                       |
| nbody                      | 71.7 ms                                                                                                                | 63.4 ms: 1.13x faster                                                                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                                                                                | 2.28 ms: 1.12x faster                                                                                                      |
| xml_etree_generate         | 58.8 ms                                                                                                                | 52.6 ms: 1.12x faster                                                                                                      |
| pyflate                    | 314 ms                                                                                                                 | 281 ms: 1.12x faster                                                                                                       |
| telco                      | 4.92 ms                                                                                                                | 4.45 ms: 1.11x faster                                                                                                      |
| fannkuch                   | 276 ms                                                                                                                 | 252 ms: 1.09x faster                                                                                                       |
| xml_etree_process          | 41.6 ms                                                                                                                | 38.3 ms: 1.09x faster                                                                                                      |
| bpe_tokeniser              | 3.00 sec                                                                                                               | 2.76 sec: 1.09x faster                                                                                                     |
| unpack_sequence            | 41.4 ns                                                                                                                | 38.7 ns: 1.07x faster                                                                                                      |
| pprint_pformat             | 1.11 sec                                                                                                               | 1.05 sec: 1.05x faster                                                                                                     |
| pprint_safe_repr           | 547 ms                                                                                                                 | 523 ms: 1.05x faster                                                                                                       |
| pickle_pure_python         | 227 us                                                                                                                 | 217 us: 1.05x faster                                                                                                       |
| pickle_list                | 3.51 us                                                                                                                | 3.37 us: 1.04x faster                                                                                                      |
| sqlglot_v2_parse           | 903 us                                                                                                                 | 867 us: 1.04x faster                                                                                                       |
| k_core                     | 1.75 sec                                                                                                               | 1.69 sec: 1.04x faster                                                                                                     |
| pickle_dict                | 20.6 us                                                                                                                | 19.8 us: 1.04x faster                                                                                                      |
| asyncio_websockets         | 315 ms                                                                                                                 | 304 ms: 1.04x faster                                                                                                       |
| scimark_sor                | 83.4 ms                                                                                                                | 80.6 ms: 1.03x faster                                                                                                      |
| connected_components       | 335 ms                                                                                                                 | 325 ms: 1.03x faster                                                                                                       |
| logging_format             | 7.26 us                                                                                                                | 7.06 us: 1.03x faster                                                                                                      |
| meteor_contest             | 77.2 ms                                                                                                                | 75.1 ms: 1.03x faster                                                                                                      |
| logging_simple             | 6.73 us                                                                                                                | 6.55 us: 1.03x faster                                                                                                      |
| sqlite_synth               | 1.57 us                                                                                                                | 1.53 us: 1.03x faster                                                                                                      |
| nqueens                    | 65.5 ms                                                                                                                | 64.0 ms: 1.02x faster                                                                                                      |
| regex_v8                   | 13.8 ms                                                                                                                | 13.5 ms: 1.02x faster                                                                                                      |
| shortest_path              | 365 ms                                                                                                                 | 358 ms: 1.02x faster                                                                                                       |
| xml_etree_iterparse        | 64.2 ms                                                                                                                | 63.0 ms: 1.02x faster                                                                                                      |
| scimark_lu                 | 61.0 ms                                                                                                                | 59.9 ms: 1.02x faster                                                                                                      |
| sqlglot_v2_transpile       | 1.11 ms                                                                                                                | 1.09 ms: 1.02x faster                                                                                                      |
| raytrace                   | 197 ms                                                                                                                 | 194 ms: 1.02x faster                                                                                                       |
| comprehensions             | 12.1 us                                                                                                                | 11.9 us: 1.02x faster                                                                                                      |
| crypto_pyaes               | 50.1 ms                                                                                                                | 49.4 ms: 1.01x faster                                                                                                      |
| python_startup             | 26.1 ms                                                                                                                | 25.7 ms: 1.01x faster                                                                                                      |
| chaos                      | 43.7 ms                                                                                                                | 43.2 ms: 1.01x faster                                                                                                      |
| genshi_text                | 17.5 ms                                                                                                                | 17.3 ms: 1.01x faster                                                                                                      |
| regex_compile              | 86.8 ms                                                                                                                | 86.2 ms: 1.01x faster                                                                                                      |
| richards_super             | 33.4 ms                                                                                                                | 33.2 ms: 1.01x faster                                                                                                      |
| bench_mp_pool              | 89.1 ms                                                                                                                | 88.7 ms: 1.01x faster                                                                                                      |
| mdp                        | 1.64 sec                                                                                                               | 1.64 sec: 1.00x slower                                                                                                     |
| coroutines                 | 13.5 ms                                                                                                                | 13.6 ms: 1.01x slower                                                                                                      |
| pidigits                   | 148 ms                                                                                                                 | 149 ms: 1.01x slower                                                                                                       |
| hexiom                     | 4.39 ms                                                                                                                | 4.42 ms: 1.01x slower                                                                                                      |
| 2to3                       | 226 ms                                                                                                                 | 228 ms: 1.01x slower                                                                                                       |
| asyncio_tcp_ssl            | 1.43 sec                                                                                                               | 1.45 sec: 1.01x slower                                                                                                     |
| sqlglot_v2_normalize       | 75.8 ms                                                                                                                | 76.8 ms: 1.01x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 342 ms                                                                                                                 | 347 ms: 1.01x slower                                                                                                       |
| sympy_sum                  | 90.1 ms                                                                                                                | 91.5 ms: 1.02x slower                                                                                                      |
| json_loads                 | 15.1 us                                                                                                                | 15.3 us: 1.02x slower                                                                                                      |
| float                      | 46.1 ms                                                                                                                | 46.9 ms: 1.02x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 342 ms                                                                                                                 | 348 ms: 1.02x slower                                                                                                       |
| sympy_integrate            | 13.3 ms                                                                                                                | 13.6 ms: 1.02x slower                                                                                                      |
| regex_dna                  | 114 ms                                                                                                                 | 116 ms: 1.02x slower                                                                                                       |
| async_tree_memoization     | 222 ms                                                                                                                 | 227 ms: 1.02x slower                                                                                                       |
| scimark_monte_carlo        | 43.8 ms                                                                                                                | 44.6 ms: 1.02x slower                                                                                                      |
| json_dumps                 | 6.99 ms                                                                                                                | 7.13 ms: 1.02x slower                                                                                                      |
| dulwich_log                | 42.2 ms                                                                                                                | 43.0 ms: 1.02x slower                                                                                                      |
| thrift                     | 530 us                                                                                                                 | 541 us: 1.02x slower                                                                                                       |
| sphinx                     | 658 ms                                                                                                                 | 673 ms: 1.02x slower                                                                                                       |
| sympy_str                  | 178 ms                                                                                                                 | 182 ms: 1.02x slower                                                                                                       |
| deepcopy_reduce            | 2.02 us                                                                                                                | 2.07 us: 1.02x slower                                                                                                      |
| pycparser                  | 738 ms                                                                                                                 | 759 ms: 1.03x slower                                                                                                       |
| coverage                   | 48.0 ms                                                                                                                | 49.4 ms: 1.03x slower                                                                                                      |
| many_optionals             | 440 us                                                                                                                 | 455 us: 1.03x slower                                                                                                       |
| sqlglot_v2_optimize        | 36.3 ms                                                                                                                | 37.5 ms: 1.03x slower                                                                                                      |
| deepcopy_memo              | 19.2 us                                                                                                                | 19.8 us: 1.03x slower                                                                                                      |
| pickle                     | 8.03 us                                                                                                                | 8.31 us: 1.03x slower                                                                                                      |
| docutils                   | 1.69 sec                                                                                                               | 1.75 sec: 1.04x slower                                                                                                     |
| unpickle_list              | 2.79 us                                                                                                                | 2.91 us: 1.04x slower                                                                                                      |
| sympy_expand               | 306 ms                                                                                                                 | 319 ms: 1.04x slower                                                                                                       |
| generators                 | 19.5 ms                                                                                                                | 20.5 ms: 1.05x slower                                                                                                      |
| spectral_norm              | 55.3 ms                                                                                                                | 58.3 ms: 1.05x slower                                                                                                      |
| genshi_xml                 | 38.0 ms                                                                                                                | 40.1 ms: 1.05x slower                                                                                                      |
| deltablue                  | 2.25 ms                                                                                                                | 2.38 ms: 1.06x slower                                                                                                      |
| async_generators           | 234 ms                                                                                                                 | 250 ms: 1.07x slower                                                                                                       |
| Geometric mean             | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (24): asyncio_tcp, go, create_gc_cycles, async_tree_io, html5lib, async_tree_none, bench_thread_pool, subparsers, richards, deepcopy, json, logging_silent, regex_effbot, pathlib, xml_etree_parse, gc_traversal, django_template, typing_runtime_protocols, async_tree_none_tg, async_tree_memoization_tg, python_startup_no_site, unpickle, async_tree_io_tg, pylint

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 62.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown