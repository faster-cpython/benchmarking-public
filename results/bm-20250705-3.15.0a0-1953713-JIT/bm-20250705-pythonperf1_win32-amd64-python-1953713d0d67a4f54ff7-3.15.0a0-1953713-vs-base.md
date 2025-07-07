# Results vs. base

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.014x faster
- HPT reliability: 68.26%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 219 ms                                                                                                                     | 220 ms: 1.01x slower                                                                                                           |
| docutils       | 1.60 sec                                                                                                                   | 1.66 sec: 1.03x slower                                                                                                         |
| html5lib       | 37.6 ms                                                                                                                    | 38.9 ms: 1.04x slower                                                                                                          |
| sphinx         | 632 ms                                                                                                                     | 641 ms: 1.01x slower                                                                                                           |
| Geometric mean | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization  | 209 ms                                                                                                                     | 206 ms: 1.02x faster                                                                                                           |
| async_tree_none         | 172 ms                                                                                                                     | 170 ms: 1.01x faster                                                                                                           |
| async_tree_cpu_io_mixed | 331 ms                                                                                                                     | 328 ms: 1.01x faster                                                                                                           |
| asyncio_tcp_ssl         | 1.38 sec                                                                                                                   | 1.44 sec: 1.04x slower                                                                                                         |
| coroutines              | 14.6 ms                                                                                                                    | 15.2 ms: 1.04x slower                                                                                                          |
| async_generators        | 231 ms                                                                                                                     | 243 ms: 1.05x slower                                                                                                           |
| asyncio_tcp             | 475 ms                                                                                                                     | 534 ms: 1.12x slower                                                                                                           |
| Geometric mean          | (ref)                                                                                                                      | 1.02x slower                                                                                                                   |

Benchmark hidden because not significant (6): async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 62.4 ms                                                                                                                    | 52.7 ms: 1.19x faster                                                                                                          |
| float          | 43.1 ms                                                                                                                    | 44.7 ms: 1.04x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 120 ms                                                                                                                     | 118 ms: 1.02x faster                                                                                                           |
| regex_compile  | 78.9 ms                                                                                                                    | 79.3 ms: 1.00x slower                                                                                                          |
| regex_effbot   | 1.58 ms                                                                                                                    | 1.60 ms: 1.01x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.00x faster                                                                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                                                                                     | 107 us: 1.24x faster                                                                                                           |
| tomli_loads          | 1.36 sec                                                                                                                   | 1.14 sec: 1.19x faster                                                                                                         |
| xml_etree_generate   | 55.3 ms                                                                                                                    | 50.8 ms: 1.09x faster                                                                                                          |
| xml_etree_process    | 38.0 ms                                                                                                                    | 35.5 ms: 1.07x faster                                                                                                          |
| xml_etree_iterparse  | 64.8 ms                                                                                                                    | 62.8 ms: 1.03x faster                                                                                                          |
| pickle_pure_python   | 208 us                                                                                                                     | 203 us: 1.03x faster                                                                                                           |
| unpickle_list        | 2.85 us                                                                                                                    | 2.78 us: 1.03x faster                                                                                                          |
| pickle               | 7.96 us                                                                                                                    | 7.82 us: 1.02x faster                                                                                                          |
| unpickle             | 8.55 us                                                                                                                    | 8.46 us: 1.01x faster                                                                                                          |
| xml_etree_parse      | 89.0 ms                                                                                                                    | 88.4 ms: 1.01x faster                                                                                                          |
| json_loads           | 14.2 us                                                                                                                    | 14.6 us: 1.03x slower                                                                                                          |
| pickle_dict          | 19.5 us                                                                                                                    | 20.8 us: 1.07x slower                                                                                                          |
| Geometric mean       | (ref)                                                                                                                      | 1.04x faster                                                                                                                   |

Benchmark hidden because not significant (2): json_dumps, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 25.6 ms                                                                                                                    | 25.8 ms: 1.01x slower                                                                                                          |
| Geometric mean | (ref)                                                                                                                      | 1.01x slower                                                                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.48 ms                                                                                                                    | 5.43 ms: 1.19x faster                                                                                                          |
| django_template | 24.4 ms                                                                                                                    | 24.2 ms: 1.01x faster                                                                                                          |
| genshi_xml      | 34.0 ms                                                                                                                    | 34.8 ms: 1.02x slower                                                                                                          |
| genshi_text     | 15.1 ms                                                                                                                    | 15.8 ms: 1.04x slower                                                                                                          |
| Geometric mean  | (ref)                                                                                                                      | 1.03x faster                                                                                                                   |

All benchmarks:
===============

| Benchmark               | results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json | results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1_win32-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python    | 133 us                                                                                                                     | 107 us: 1.24x faster                                                                                                           |
| mako                    | 6.48 ms                                                                                                                    | 5.43 ms: 1.19x faster                                                                                                          |
| scimark_fft             | 180 ms                                                                                                                     | 151 ms: 1.19x faster                                                                                                           |
| tomli_loads             | 1.36 sec                                                                                                                   | 1.14 sec: 1.19x faster                                                                                                         |
| nbody                   | 62.4 ms                                                                                                                    | 52.7 ms: 1.19x faster                                                                                                          |
| fannkuch                | 260 ms                                                                                                                     | 219 ms: 1.18x faster                                                                                                           |
| pyflate                 | 292 ms                                                                                                                     | 254 ms: 1.15x faster                                                                                                           |
| bpe_tokeniser           | 2.96 sec                                                                                                                   | 2.60 sec: 1.14x faster                                                                                                         |
| scimark_sparse_mat_mult | 2.54 ms                                                                                                                    | 2.23 ms: 1.14x faster                                                                                                          |
| xml_etree_generate      | 55.3 ms                                                                                                                    | 50.8 ms: 1.09x faster                                                                                                          |
| telco                   | 4.54 ms                                                                                                                    | 4.19 ms: 1.08x faster                                                                                                          |
| xml_etree_process       | 38.0 ms                                                                                                                    | 35.5 ms: 1.07x faster                                                                                                          |
| pprint_safe_repr        | 481 ms                                                                                                                     | 449 ms: 1.07x faster                                                                                                           |
| pprint_pformat          | 980 ms                                                                                                                     | 918 ms: 1.07x faster                                                                                                           |
| k_core                  | 1.71 sec                                                                                                                   | 1.62 sec: 1.06x faster                                                                                                         |
| connected_components    | 331 ms                                                                                                                     | 316 ms: 1.05x faster                                                                                                           |
| nqueens                 | 61.0 ms                                                                                                                    | 58.9 ms: 1.04x faster                                                                                                          |
| xml_etree_iterparse     | 64.8 ms                                                                                                                    | 62.8 ms: 1.03x faster                                                                                                          |
| pickle_pure_python      | 208 us                                                                                                                     | 203 us: 1.03x faster                                                                                                           |
| unpickle_list           | 2.85 us                                                                                                                    | 2.78 us: 1.03x faster                                                                                                          |
| sqlite_synth            | 1.59 us                                                                                                                    | 1.55 us: 1.02x faster                                                                                                          |
| regex_dna               | 120 ms                                                                                                                     | 118 ms: 1.02x faster                                                                                                           |
| crypto_pyaes            | 47.1 ms                                                                                                                    | 46.1 ms: 1.02x faster                                                                                                          |
| pickle                  | 7.96 us                                                                                                                    | 7.82 us: 1.02x faster                                                                                                          |
| sqlglot_v2_parse        | 807 us                                                                                                                     | 793 us: 1.02x faster                                                                                                           |
| sqlglot_v2_transpile    | 1.01 ms                                                                                                                    | 995 us: 1.02x faster                                                                                                           |
| async_tree_memoization  | 209 ms                                                                                                                     | 206 ms: 1.02x faster                                                                                                           |
| shortest_path           | 364 ms                                                                                                                     | 360 ms: 1.01x faster                                                                                                           |
| async_tree_none         | 172 ms                                                                                                                     | 170 ms: 1.01x faster                                                                                                           |
| unpickle                | 8.55 us                                                                                                                    | 8.46 us: 1.01x faster                                                                                                          |
| async_tree_cpu_io_mixed | 331 ms                                                                                                                     | 328 ms: 1.01x faster                                                                                                           |
| meteor_contest          | 71.5 ms                                                                                                                    | 70.9 ms: 1.01x faster                                                                                                          |
| pathlib                 | 32.1 ms                                                                                                                    | 31.9 ms: 1.01x faster                                                                                                          |
| xml_etree_parse         | 89.0 ms                                                                                                                    | 88.4 ms: 1.01x faster                                                                                                          |
| django_template         | 24.4 ms                                                                                                                    | 24.2 ms: 1.01x faster                                                                                                          |
| comprehensions          | 10.6 us                                                                                                                    | 10.6 us: 1.00x faster                                                                                                          |
| regex_compile           | 78.9 ms                                                                                                                    | 79.3 ms: 1.00x slower                                                                                                          |
| 2to3                    | 219 ms                                                                                                                     | 220 ms: 1.01x slower                                                                                                           |
| deepcopy                | 169 us                                                                                                                     | 170 us: 1.01x slower                                                                                                           |
| python_startup          | 25.6 ms                                                                                                                    | 25.8 ms: 1.01x slower                                                                                                          |
| sympy_sum               | 86.6 ms                                                                                                                    | 87.4 ms: 1.01x slower                                                                                                          |
| regex_effbot            | 1.58 ms                                                                                                                    | 1.60 ms: 1.01x slower                                                                                                          |
| sphinx                  | 632 ms                                                                                                                     | 641 ms: 1.01x slower                                                                                                           |
| logging_silent          | 55.1 ns                                                                                                                    | 55.9 ns: 1.01x slower                                                                                                          |
| raytrace                | 177 ms                                                                                                                     | 180 ms: 1.02x slower                                                                                                           |
| genshi_xml              | 34.0 ms                                                                                                                    | 34.8 ms: 1.02x slower                                                                                                          |
| richards                | 26.9 ms                                                                                                                    | 27.6 ms: 1.02x slower                                                                                                          |
| sympy_str               | 167 ms                                                                                                                     | 171 ms: 1.03x slower                                                                                                           |
| sympy_expand            | 286 ms                                                                                                                     | 294 ms: 1.03x slower                                                                                                           |
| json_loads              | 14.2 us                                                                                                                    | 14.6 us: 1.03x slower                                                                                                          |
| many_optionals          | 431 us                                                                                                                     | 445 us: 1.03x slower                                                                                                           |
| go                      | 75.9 ms                                                                                                                    | 78.4 ms: 1.03x slower                                                                                                          |
| richards_super          | 30.5 ms                                                                                                                    | 31.5 ms: 1.03x slower                                                                                                          |
| docutils                | 1.60 sec                                                                                                                   | 1.66 sec: 1.03x slower                                                                                                         |
| html5lib                | 37.6 ms                                                                                                                    | 38.9 ms: 1.04x slower                                                                                                          |
| sympy_integrate         | 12.3 ms                                                                                                                    | 12.7 ms: 1.04x slower                                                                                                          |
| hexiom                  | 4.01 ms                                                                                                                    | 4.16 ms: 1.04x slower                                                                                                          |
| asyncio_tcp_ssl         | 1.38 sec                                                                                                                   | 1.44 sec: 1.04x slower                                                                                                         |
| float                   | 43.1 ms                                                                                                                    | 44.7 ms: 1.04x slower                                                                                                          |
| sqlglot_v2_optimize     | 33.9 ms                                                                                                                    | 35.2 ms: 1.04x slower                                                                                                          |
| coroutines              | 14.6 ms                                                                                                                    | 15.2 ms: 1.04x slower                                                                                                          |
| chaos                   | 39.7 ms                                                                                                                    | 41.3 ms: 1.04x slower                                                                                                          |
| genshi_text             | 15.1 ms                                                                                                                    | 15.8 ms: 1.04x slower                                                                                                          |
| scimark_monte_carlo     | 39.3 ms                                                                                                                    | 41.0 ms: 1.04x slower                                                                                                          |
| async_generators        | 231 ms                                                                                                                     | 243 ms: 1.05x slower                                                                                                           |
| deepcopy_memo           | 17.4 us                                                                                                                    | 18.3 us: 1.05x slower                                                                                                          |
| scimark_sor             | 75.7 ms                                                                                                                    | 79.9 ms: 1.06x slower                                                                                                          |
| deltablue               | 2.12 ms                                                                                                                    | 2.26 ms: 1.06x slower                                                                                                          |
| scimark_lu              | 57.2 ms                                                                                                                    | 61.0 ms: 1.07x slower                                                                                                          |
| pickle_dict             | 19.5 us                                                                                                                    | 20.8 us: 1.07x slower                                                                                                          |
| spectral_norm           | 62.9 ms                                                                                                                    | 68.3 ms: 1.09x slower                                                                                                          |
| unpack_sequence         | 36.8 ns                                                                                                                    | 40.5 ns: 1.10x slower                                                                                                          |
| asyncio_tcp             | 475 ms                                                                                                                     | 534 ms: 1.12x slower                                                                                                           |
| Geometric mean          | (ref)                                                                                                                      | 1.01x faster                                                                                                                   |

Benchmark hidden because not significant (29): regex_v8, gc_traversal, async_tree_io, json_dumps, sqlglot_v2_normalize, mdp, pickle_list, logging_format, coverage, pycparser, json, dulwich_log, async_tree_none_tg, thrift, bench_mp_pool, deepcopy_reduce, logging_simple, pidigits, async_tree_cpu_io_mixed_tg, generators, python_startup_no_site, typing_runtime_protocols, create_gc_cycles, async_tree_io_tg, subparsers, async_tree_memoization_tg, asyncio_websockets, bench_thread_pool, pylint

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 68.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown