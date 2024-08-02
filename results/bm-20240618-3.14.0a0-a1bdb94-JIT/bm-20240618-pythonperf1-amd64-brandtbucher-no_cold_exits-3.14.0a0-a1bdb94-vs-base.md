# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-amd64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.00x faster
- HPT reliability: 89.85%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 230 ms                                                                     | 227 ms: 1.01x faster                                                      |
| docutils       | 1.74 sec                                                                   | 1.73 sec: 1.00x faster                                                    |
| html5lib       | 36.0 ms                                                                    | 36.4 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                                     | 149 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                              |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                     | 115 ms: 1.04x faster                                                      |
| regex_effbot   | 1.58 ms                                                                    | 1.56 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                              |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle               | 7.47 us                                                                    | 7.20 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 60.6 ms                                                                    | 59.6 ms: 1.02x faster                                                     |
| tomli_loads          | 1.19 sec                                                                   | 1.18 sec: 1.01x faster                                                    |
| unpickle             | 8.84 us                                                                    | 8.78 us: 1.01x faster                                                     |
| pickle_pure_python   | 167 us                                                                     | 168 us: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                                    | 14.1 us: 1.01x slower                                                     |
| xml_etree_process    | 35.5 ms                                                                    | 36.1 ms: 1.02x slower                                                     |
| pickle_dict          | 17.6 us                                                                    | 17.9 us: 1.02x slower                                                     |
| json_dumps           | 5.57 ms                                                                    | 5.69 ms: 1.02x slower                                                     |
| xml_etree_generate   | 50.7 ms                                                                    | 51.7 ms: 1.02x slower                                                     |
| unpickle_pure_python | 121 us                                                                     | 125 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                              |

Benchmark hidden because not significant (3): pickle_list, xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 18.0 ms                                                                    | 16.6 ms: 1.08x faster                                                     |
| python_startup         | 22.0 ms                                                                    | 20.4 ms: 1.08x faster                                                     |
| Geometric mean         | (ref)                                                                      | 1.08x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 24.5 ms                                                                    | 24.0 ms: 1.02x faster                                                     |
| genshi_text     | 17.5 ms                                                                    | 17.3 ms: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                              |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark               | bm-20240618-pythonperf1-amd64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-pythonperf1-amd64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:--------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site  | 18.0 ms                                                                    | 16.6 ms: 1.08x faster                                                     |
| python_startup          | 22.0 ms                                                                    | 20.4 ms: 1.08x faster                                                     |
| richards                | 30.1 ms                                                                    | 28.1 ms: 1.07x faster                                                     |
| richards_super          | 33.7 ms                                                                    | 31.8 ms: 1.06x faster                                                     |
| regex_dna               | 120 ms                                                                     | 115 ms: 1.04x faster                                                      |
| pickle                  | 7.47 us                                                                    | 7.20 us: 1.04x faster                                                     |
| asyncio_tcp             | 478 ms                                                                     | 466 ms: 1.02x faster                                                      |
| django_template         | 24.5 ms                                                                    | 24.0 ms: 1.02x faster                                                     |
| deepcopy                | 172 us                                                                     | 169 us: 1.02x faster                                                      |
| logging_silent          | 54.0 ns                                                                    | 53.1 ns: 1.02x faster                                                     |
| sqlglot_optimize        | 35.6 ms                                                                    | 35.0 ms: 1.02x faster                                                     |
| regex_effbot            | 1.58 ms                                                                    | 1.56 ms: 1.02x faster                                                     |
| logging_simple          | 5.54 us                                                                    | 5.46 us: 1.02x faster                                                     |
| xml_etree_iterparse     | 60.6 ms                                                                    | 59.6 ms: 1.02x faster                                                     |
| bench_mp_pool           | 69.6 ms                                                                    | 68.6 ms: 1.02x faster                                                     |
| create_gc_cycles        | 919 us                                                                     | 905 us: 1.02x faster                                                      |
| sympy_expand            | 302 ms                                                                     | 297 ms: 1.02x faster                                                      |
| logging_format          | 6.01 us                                                                    | 5.92 us: 1.02x faster                                                     |
| coverage                | 45.2 ms                                                                    | 44.5 ms: 1.02x faster                                                     |
| sympy_sum               | 92.0 ms                                                                    | 90.8 ms: 1.01x faster                                                     |
| 2to3                    | 230 ms                                                                     | 227 ms: 1.01x faster                                                      |
| sympy_str               | 175 ms                                                                     | 173 ms: 1.01x faster                                                      |
| thrift                  | 498 us                                                                     | 491 us: 1.01x faster                                                      |
| genshi_text             | 17.5 ms                                                                    | 17.3 ms: 1.01x faster                                                     |
| meteor_contest          | 72.8 ms                                                                    | 72.1 ms: 1.01x faster                                                     |
| pathlib                 | 75.5 ms                                                                    | 74.9 ms: 1.01x faster                                                     |
| deepcopy_reduce         | 1.73 us                                                                    | 1.72 us: 1.01x faster                                                     |
| tomli_loads             | 1.19 sec                                                                   | 1.18 sec: 1.01x faster                                                    |
| telco                   | 4.50 ms                                                                    | 4.47 ms: 1.01x faster                                                     |
| unpickle                | 8.84 us                                                                    | 8.78 us: 1.01x faster                                                     |
| gc_traversal            | 1.57 ms                                                                    | 1.56 ms: 1.01x faster                                                     |
| sqlglot_transpile       | 1.00 ms                                                                    | 998 us: 1.01x faster                                                      |
| sympy_integrate         | 13.7 ms                                                                    | 13.6 ms: 1.00x faster                                                     |
| docutils                | 1.74 sec                                                                   | 1.73 sec: 1.00x faster                                                    |
| sqlglot_parse           | 774 us                                                                     | 771 us: 1.00x faster                                                      |
| pidigits                | 149 ms                                                                     | 149 ms: 1.00x slower                                                      |
| pickle_pure_python      | 167 us                                                                     | 168 us: 1.01x slower                                                      |
| coroutines              | 12.6 ms                                                                    | 12.7 ms: 1.01x slower                                                     |
| crypto_pyaes            | 40.5 ms                                                                    | 40.8 ms: 1.01x slower                                                     |
| generators              | 19.8 ms                                                                    | 19.9 ms: 1.01x slower                                                     |
| raytrace                | 169 ms                                                                     | 170 ms: 1.01x slower                                                      |
| html5lib                | 36.0 ms                                                                    | 36.4 ms: 1.01x slower                                                     |
| pprint_safe_repr        | 449 ms                                                                     | 454 ms: 1.01x slower                                                      |
| json_loads              | 13.9 us                                                                    | 14.1 us: 1.01x slower                                                     |
| spectral_norm           | 45.0 ms                                                                    | 45.7 ms: 1.01x slower                                                     |
| scimark_monte_carlo     | 36.6 ms                                                                    | 37.2 ms: 1.02x slower                                                     |
| xml_etree_process       | 35.5 ms                                                                    | 36.1 ms: 1.02x slower                                                     |
| pickle_dict             | 17.6 us                                                                    | 17.9 us: 1.02x slower                                                     |
| fannkuch                | 221 ms                                                                     | 225 ms: 1.02x slower                                                      |
| json_dumps              | 5.57 ms                                                                    | 5.69 ms: 1.02x slower                                                     |
| xml_etree_generate      | 50.7 ms                                                                    | 51.7 ms: 1.02x slower                                                     |
| scimark_fft             | 148 ms                                                                     | 151 ms: 1.02x slower                                                      |
| scimark_lu              | 67.7 ms                                                                    | 69.3 ms: 1.02x slower                                                     |
| nqueens                 | 58.5 ms                                                                    | 60.0 ms: 1.03x slower                                                     |
| chaos                   | 38.1 ms                                                                    | 39.1 ms: 1.03x slower                                                     |
| unpickle_pure_python    | 121 us                                                                     | 125 us: 1.03x slower                                                      |
| async_generators        | 240 ms                                                                     | 248 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult | 2.12 ms                                                                    | 2.19 ms: 1.03x slower                                                     |
| mdp                     | 1.38 sec                                                                   | 1.44 sec: 1.04x slower                                                    |
| Geometric mean          | (ref)                                                                      | 1.00x faster                                                              |

Benchmark hidden because not significant (33): asyncio_tcp_ssl, regex_v8, pickle_list, async_tree_none_tg, nbody, pylint, typing_runtime_protocols, async_tree_none, xml_etree_parse, regex_compile, tornado_http, sqlite_synth, comprehensions, pyflate, async_tree_cpu_io_mixed_tg, float, deltablue, genshi_xml, async_tree_memoization, scimark_sor, hexiom, go, pprint_pformat, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, json, async_tree_io, unpickle_list, deepcopy_memo, bench_thread_pool, mako, pycparser

# HPT report

- Reliability score: 89.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown