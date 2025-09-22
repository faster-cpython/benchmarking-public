# Results vs. base

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.031x faster
- HPT reliability: 93.27%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                                                                               | 220 ms: 1.01x slower                                                                                                     |
| docutils       | 1.60 sec                                                                                                             | 1.67 sec: 1.05x slower                                                                                                   |
| sphinx         | 624 ms                                                                                                               | 644 ms: 1.03x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 195 ms                                                                                                               | 166 ms: 1.17x faster                                                                                                     |
| async_tree_none            | 199 ms                                                                                                               | 174 ms: 1.15x faster                                                                                                     |
| async_tree_memoization     | 233 ms                                                                                                               | 204 ms: 1.14x faster                                                                                                     |
| async_tree_memoization_tg  | 238 ms                                                                                                               | 210 ms: 1.14x faster                                                                                                     |
| async_tree_io              | 444 ms                                                                                                               | 393 ms: 1.13x faster                                                                                                     |
| async_tree_io_tg           | 432 ms                                                                                                               | 386 ms: 1.12x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 350 ms                                                                                                               | 332 ms: 1.06x faster                                                                                                     |
| asyncio_websockets         | 170 ms                                                                                                               | 162 ms: 1.05x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 355 ms                                                                                                               | 338 ms: 1.05x faster                                                                                                     |
| coroutines                 | 14.9 ms                                                                                                              | 14.5 ms: 1.03x faster                                                                                                    |
| asyncio_tcp_ssl            | 1.38 sec                                                                                                             | 1.43 sec: 1.04x slower                                                                                                   |
| async_generators           | 231 ms                                                                                                               | 241 ms: 1.04x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.07x faster                                                                                                             |

Benchmark hidden because not significant (1): asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 63.7 ms                                                                                                              | 54.6 ms: 1.17x faster                                                                                                    |
| float          | 43.7 ms                                                                                                              | 40.2 ms: 1.09x faster                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 79.7 ms                                                                                                              | 78.7 ms: 1.01x faster                                                                                                    |
| regex_v8       | 14.2 ms                                                                                                              | 14.8 ms: 1.05x slower                                                                                                    |
| regex_effbot   | 1.48 ms                                                                                                              | 1.59 ms: 1.07x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 137 us                                                                                                               | 106 us: 1.29x faster                                                                                                     |
| tomli_loads          | 1.37 sec                                                                                                             | 1.09 sec: 1.26x faster                                                                                                   |
| xml_etree_generate   | 55.2 ms                                                                                                              | 50.0 ms: 1.10x faster                                                                                                    |
| xml_etree_process    | 39.0 ms                                                                                                              | 35.4 ms: 1.10x faster                                                                                                    |
| unpickle_list        | 2.99 us                                                                                                              | 2.76 us: 1.08x faster                                                                                                    |
| pickle_list          | 3.40 us                                                                                                              | 3.25 us: 1.05x faster                                                                                                    |
| pickle_dict          | 20.7 us                                                                                                              | 19.8 us: 1.05x faster                                                                                                    |
| pickle_pure_python   | 212 us                                                                                                               | 205 us: 1.03x faster                                                                                                     |
| pickle               | 7.87 us                                                                                                              | 7.73 us: 1.02x faster                                                                                                    |
| xml_etree_parse      | 86.8 ms                                                                                                              | 87.5 ms: 1.01x slower                                                                                                    |
| json_loads           | 14.0 us                                                                                                              | 14.2 us: 1.02x slower                                                                                                    |
| unpickle             | 8.38 us                                                                                                              | 8.71 us: 1.04x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 25.2 ms                                                                                                              | 25.5 ms: 1.01x slower                                                                                                    |
| python_startup_no_site | 18.7 ms                                                                                                              | 19.3 ms: 1.03x slower                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.70 ms                                                                                                              | 5.36 ms: 1.25x faster                                                                                                    |
| genshi_text    | 16.1 ms                                                                                                              | 15.5 ms: 1.04x faster                                                                                                    |
| genshi_xml     | 35.5 ms                                                                                                              | 36.6 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | results/bm-20250920-3.15.0a0-20d5494/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json | results/bm-20250920-3.15.0a0-20d5494-JIT/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 137 us                                                                                                               | 106 us: 1.29x faster                                                                                                     |
| tomli_loads                | 1.37 sec                                                                                                             | 1.09 sec: 1.26x faster                                                                                                   |
| mako                       | 6.70 ms                                                                                                              | 5.36 ms: 1.25x faster                                                                                                    |
| scimark_fft                | 187 ms                                                                                                               | 154 ms: 1.22x faster                                                                                                     |
| fannkuch                   | 263 ms                                                                                                               | 216 ms: 1.22x faster                                                                                                     |
| async_tree_none_tg         | 195 ms                                                                                                               | 166 ms: 1.17x faster                                                                                                     |
| nbody                      | 63.7 ms                                                                                                              | 54.6 ms: 1.17x faster                                                                                                    |
| bpe_tokeniser              | 2.93 sec                                                                                                             | 2.54 sec: 1.15x faster                                                                                                   |
| pprint_pformat             | 993 ms                                                                                                               | 864 ms: 1.15x faster                                                                                                     |
| async_tree_none            | 199 ms                                                                                                               | 174 ms: 1.15x faster                                                                                                     |
| async_tree_memoization     | 233 ms                                                                                                               | 204 ms: 1.14x faster                                                                                                     |
| async_tree_memoization_tg  | 238 ms                                                                                                               | 210 ms: 1.14x faster                                                                                                     |
| async_tree_io              | 444 ms                                                                                                               | 393 ms: 1.13x faster                                                                                                     |
| pyflate                    | 282 ms                                                                                                               | 251 ms: 1.13x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.54 ms                                                                                                              | 2.27 ms: 1.12x faster                                                                                                    |
| async_tree_io_tg           | 432 ms                                                                                                               | 386 ms: 1.12x faster                                                                                                     |
| pprint_safe_repr           | 487 ms                                                                                                               | 439 ms: 1.11x faster                                                                                                     |
| xml_etree_generate         | 55.2 ms                                                                                                              | 50.0 ms: 1.10x faster                                                                                                    |
| xml_etree_process          | 39.0 ms                                                                                                              | 35.4 ms: 1.10x faster                                                                                                    |
| unpack_sequence            | 38.0 ns                                                                                                              | 34.5 ns: 1.10x faster                                                                                                    |
| float                      | 43.7 ms                                                                                                              | 40.2 ms: 1.09x faster                                                                                                    |
| unpickle_list              | 2.99 us                                                                                                              | 2.76 us: 1.08x faster                                                                                                    |
| raytrace                   | 188 ms                                                                                                               | 176 ms: 1.07x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 350 ms                                                                                                               | 332 ms: 1.06x faster                                                                                                     |
| crypto_pyaes               | 47.9 ms                                                                                                              | 45.3 ms: 1.06x faster                                                                                                    |
| deepcopy_memo              | 17.7 us                                                                                                              | 16.8 us: 1.06x faster                                                                                                    |
| asyncio_websockets         | 170 ms                                                                                                               | 162 ms: 1.05x faster                                                                                                     |
| sqlglot_v2_parse           | 829 us                                                                                                               | 789 us: 1.05x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 355 ms                                                                                                               | 338 ms: 1.05x faster                                                                                                     |
| telco                      | 4.29 ms                                                                                                              | 4.08 ms: 1.05x faster                                                                                                    |
| pickle_list                | 3.40 us                                                                                                              | 3.25 us: 1.05x faster                                                                                                    |
| spectral_norm              | 65.3 ms                                                                                                              | 62.4 ms: 1.05x faster                                                                                                    |
| pickle_dict                | 20.7 us                                                                                                              | 19.8 us: 1.05x faster                                                                                                    |
| comprehensions             | 11.2 us                                                                                                              | 10.7 us: 1.04x faster                                                                                                    |
| genshi_text                | 16.1 ms                                                                                                              | 15.5 ms: 1.04x faster                                                                                                    |
| pickle_pure_python         | 212 us                                                                                                               | 205 us: 1.03x faster                                                                                                     |
| k_core                     | 1.66 sec                                                                                                             | 1.60 sec: 1.03x faster                                                                                                   |
| hexiom                     | 4.21 ms                                                                                                              | 4.08 ms: 1.03x faster                                                                                                    |
| deltablue                  | 2.25 ms                                                                                                              | 2.18 ms: 1.03x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.03 ms                                                                                                              | 996 us: 1.03x faster                                                                                                     |
| coroutines                 | 14.9 ms                                                                                                              | 14.5 ms: 1.03x faster                                                                                                    |
| shortest_path              | 364 ms                                                                                                               | 354 ms: 1.03x faster                                                                                                     |
| chaos                      | 41.5 ms                                                                                                              | 40.5 ms: 1.02x faster                                                                                                    |
| deepcopy                   | 168 us                                                                                                               | 165 us: 1.02x faster                                                                                                     |
| pickle                     | 7.87 us                                                                                                              | 7.73 us: 1.02x faster                                                                                                    |
| nqueens                    | 62.3 ms                                                                                                              | 61.3 ms: 1.02x faster                                                                                                    |
| pathlib                    | 29.9 ms                                                                                                              | 29.4 ms: 1.01x faster                                                                                                    |
| regex_compile              | 79.7 ms                                                                                                              | 78.7 ms: 1.01x faster                                                                                                    |
| logging_silent             | 55.2 ns                                                                                                              | 54.5 ns: 1.01x faster                                                                                                    |
| connected_components       | 325 ms                                                                                                               | 323 ms: 1.01x faster                                                                                                     |
| meteor_contest             | 73.6 ms                                                                                                              | 74.2 ms: 1.01x slower                                                                                                    |
| xml_etree_parse            | 86.8 ms                                                                                                              | 87.5 ms: 1.01x slower                                                                                                    |
| scimark_monte_carlo        | 39.8 ms                                                                                                              | 40.1 ms: 1.01x slower                                                                                                    |
| python_startup             | 25.2 ms                                                                                                              | 25.5 ms: 1.01x slower                                                                                                    |
| 2to3                       | 217 ms                                                                                                               | 220 ms: 1.01x slower                                                                                                     |
| bench_mp_pool              | 90.0 ms                                                                                                              | 91.4 ms: 1.01x slower                                                                                                    |
| json_loads                 | 14.0 us                                                                                                              | 14.2 us: 1.02x slower                                                                                                    |
| logging_simple             | 5.97 us                                                                                                              | 6.06 us: 1.02x slower                                                                                                    |
| logging_format             | 6.42 us                                                                                                              | 6.54 us: 1.02x slower                                                                                                    |
| mdp                        | 792 ms                                                                                                               | 807 ms: 1.02x slower                                                                                                     |
| richards_super             | 30.8 ms                                                                                                              | 31.4 ms: 1.02x slower                                                                                                    |
| richards                   | 27.2 ms                                                                                                              | 27.8 ms: 1.02x slower                                                                                                    |
| json                       | 2.92 ms                                                                                                              | 2.97 ms: 1.02x slower                                                                                                    |
| create_gc_cycles           | 1.25 ms                                                                                                              | 1.28 ms: 1.02x slower                                                                                                    |
| subparsers                 | 31.1 ms                                                                                                              | 31.8 ms: 1.02x slower                                                                                                    |
| pylint                     | 193 ms                                                                                                               | 198 ms: 1.03x slower                                                                                                     |
| sqlglot_v2_optimize        | 33.8 ms                                                                                                              | 34.7 ms: 1.03x slower                                                                                                    |
| sphinx                     | 624 ms                                                                                                               | 644 ms: 1.03x slower                                                                                                     |
| python_startup_no_site     | 18.7 ms                                                                                                              | 19.3 ms: 1.03x slower                                                                                                    |
| genshi_xml                 | 35.5 ms                                                                                                              | 36.6 ms: 1.03x slower                                                                                                    |
| thrift                     | 504 us                                                                                                               | 522 us: 1.04x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.38 sec                                                                                                             | 1.43 sec: 1.04x slower                                                                                                   |
| sympy_str                  | 166 ms                                                                                                               | 172 ms: 1.04x slower                                                                                                     |
| unpickle                   | 8.38 us                                                                                                              | 8.71 us: 1.04x slower                                                                                                    |
| gc_traversal               | 2.05 ms                                                                                                              | 2.13 ms: 1.04x slower                                                                                                    |
| sympy_expand               | 281 ms                                                                                                               | 293 ms: 1.04x slower                                                                                                     |
| async_generators           | 231 ms                                                                                                               | 241 ms: 1.04x slower                                                                                                     |
| sympy_sum                  | 84.4 ms                                                                                                              | 88.1 ms: 1.04x slower                                                                                                    |
| docutils                   | 1.60 sec                                                                                                             | 1.67 sec: 1.05x slower                                                                                                   |
| sympy_integrate            | 12.2 ms                                                                                                              | 12.8 ms: 1.05x slower                                                                                                    |
| regex_v8                   | 14.2 ms                                                                                                              | 14.8 ms: 1.05x slower                                                                                                    |
| scimark_sor                | 74.2 ms                                                                                                              | 78.2 ms: 1.05x slower                                                                                                    |
| dulwich_log                | 38.4 ms                                                                                                              | 40.7 ms: 1.06x slower                                                                                                    |
| many_optionals             | 559 us                                                                                                               | 597 us: 1.07x slower                                                                                                     |
| regex_effbot               | 1.48 ms                                                                                                              | 1.59 ms: 1.07x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (17): deepcopy_reduce, xml_etree_iterparse, sqlite_synth, coverage, django_template, go, sqlglot_v2_normalize, pidigits, regex_dna, pycparser, typing_runtime_protocols, json_dumps, html5lib, generators, scimark_lu, asyncio_tcp, bench_thread_pool

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 93.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown