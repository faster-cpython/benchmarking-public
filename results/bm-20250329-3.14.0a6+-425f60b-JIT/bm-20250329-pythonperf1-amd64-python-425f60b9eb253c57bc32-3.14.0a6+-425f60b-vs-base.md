# Results vs. base

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.004x slower
- HPT reliability: 93.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                                                                 | 224 ms: 1.02x slower                                                                                                       |
| docutils       | 1.65 sec                                                                                                               | 1.72 sec: 1.04x slower                                                                                                     |
| html5lib       | 39.0 ms                                                                                                                | 39.5 ms: 1.01x slower                                                                                                      |
| sphinx         | 653 ms                                                                                                                 | 667 ms: 1.02x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|--------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg | 176 ms                                                                                                                 | 174 ms: 1.01x faster                                                                                                       |
| async_generators   | 223 ms                                                                                                                 | 244 ms: 1.09x slower                                                                                                       |
| Geometric mean     | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (11): asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, coroutines, async_tree_cpu_io_mixed, async_tree_none, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_io, async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 64.2 ms                                                                                                                | 60.9 ms: 1.05x faster                                                                                                      |
| float          | 44.7 ms                                                                                                                | 47.0 ms: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 82.3 ms                                                                                                                | 83.4 ms: 1.01x slower                                                                                                      |
| regex_dna      | 114 ms                                                                                                                 | 120 ms: 1.05x slower                                                                                                       |
| regex_v8       | 13.4 ms                                                                                                                | 14.2 ms: 1.06x slower                                                                                                      |
| regex_effbot   | 1.39 ms                                                                                                                | 1.48 ms: 1.07x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.05x slower                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 140 us                                                                                                                 | 122 us: 1.15x faster                                                                                                       |
| tomli_loads          | 1.41 sec                                                                                                               | 1.25 sec: 1.13x faster                                                                                                     |
| xml_etree_generate   | 57.2 ms                                                                                                                | 52.0 ms: 1.10x faster                                                                                                      |
| xml_etree_process    | 40.9 ms                                                                                                                | 37.8 ms: 1.08x faster                                                                                                      |
| pickle_list          | 3.58 us                                                                                                                | 3.33 us: 1.08x faster                                                                                                      |
| pickle_dict          | 21.3 us                                                                                                                | 20.3 us: 1.05x faster                                                                                                      |
| xml_etree_iterparse  | 64.1 ms                                                                                                                | 62.1 ms: 1.03x faster                                                                                                      |
| json_loads           | 15.1 us                                                                                                                | 15.0 us: 1.01x faster                                                                                                      |
| pickle               | 8.52 us                                                                                                                | 8.56 us: 1.01x slower                                                                                                      |
| unpickle_list        | 2.76 us                                                                                                                | 2.80 us: 1.01x slower                                                                                                      |
| pickle_pure_python   | 216 us                                                                                                                 | 219 us: 1.01x slower                                                                                                       |
| unpickle             | 8.27 us                                                                                                                | 8.80 us: 1.06x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.71 ms                                                                                                                | 5.66 ms: 1.19x faster                                                                                                      |
| genshi_text    | 15.8 ms                                                                                                                | 16.4 ms: 1.04x slower                                                                                                      |
| genshi_xml     | 34.2 ms                                                                                                                | 36.5 ms: 1.07x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.02x faster                                                                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json | results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 2.69 ms                                                                                                                | 2.13 ms: 1.26x faster                                                                                                      |
| scimark_fft              | 185 ms                                                                                                                 | 154 ms: 1.20x faster                                                                                                       |
| mako                     | 6.71 ms                                                                                                                | 5.66 ms: 1.19x faster                                                                                                      |
| unpickle_pure_python     | 140 us                                                                                                                 | 122 us: 1.15x faster                                                                                                       |
| tomli_loads              | 1.41 sec                                                                                                               | 1.25 sec: 1.13x faster                                                                                                     |
| pyflate                  | 291 ms                                                                                                                 | 265 ms: 1.10x faster                                                                                                       |
| xml_etree_generate       | 57.2 ms                                                                                                                | 52.0 ms: 1.10x faster                                                                                                      |
| xml_etree_process        | 40.9 ms                                                                                                                | 37.8 ms: 1.08x faster                                                                                                      |
| pickle_list              | 3.58 us                                                                                                                | 3.33 us: 1.08x faster                                                                                                      |
| telco                    | 4.87 ms                                                                                                                | 4.55 ms: 1.07x faster                                                                                                      |
| bpe_tokeniser            | 2.93 sec                                                                                                               | 2.74 sec: 1.07x faster                                                                                                     |
| nbody                    | 64.2 ms                                                                                                                | 60.9 ms: 1.05x faster                                                                                                      |
| pickle_dict              | 21.3 us                                                                                                                | 20.3 us: 1.05x faster                                                                                                      |
| pprint_pformat           | 1.07 sec                                                                                                               | 1.03 sec: 1.04x faster                                                                                                     |
| xml_etree_iterparse      | 64.1 ms                                                                                                                | 62.1 ms: 1.03x faster                                                                                                      |
| connected_components     | 336 ms                                                                                                                 | 327 ms: 1.03x faster                                                                                                       |
| nqueens                  | 63.5 ms                                                                                                                | 62.1 ms: 1.02x faster                                                                                                      |
| sqlite_synth             | 1.58 us                                                                                                                | 1.55 us: 1.02x faster                                                                                                      |
| pprint_safe_repr         | 521 ms                                                                                                                 | 511 ms: 1.02x faster                                                                                                       |
| fannkuch                 | 260 ms                                                                                                                 | 255 ms: 1.02x faster                                                                                                       |
| k_core                   | 1.71 sec                                                                                                               | 1.68 sec: 1.02x faster                                                                                                     |
| scimark_lu               | 61.6 ms                                                                                                                | 60.5 ms: 1.02x faster                                                                                                      |
| shortest_path            | 366 ms                                                                                                                 | 360 ms: 1.02x faster                                                                                                       |
| gc_traversal             | 2.08 ms                                                                                                                | 2.05 ms: 1.01x faster                                                                                                      |
| json_loads               | 15.1 us                                                                                                                | 15.0 us: 1.01x faster                                                                                                      |
| async_tree_none_tg       | 176 ms                                                                                                                 | 174 ms: 1.01x faster                                                                                                       |
| mdp                      | 799 ms                                                                                                                 | 792 ms: 1.01x faster                                                                                                       |
| raytrace                 | 181 ms                                                                                                                 | 180 ms: 1.01x faster                                                                                                       |
| pickle                   | 8.52 us                                                                                                                | 8.56 us: 1.01x slower                                                                                                      |
| meteor_contest           | 76.2 ms                                                                                                                | 76.7 ms: 1.01x slower                                                                                                      |
| logging_format           | 6.88 us                                                                                                                | 6.95 us: 1.01x slower                                                                                                      |
| html5lib                 | 39.0 ms                                                                                                                | 39.5 ms: 1.01x slower                                                                                                      |
| unpickle_list            | 2.76 us                                                                                                                | 2.80 us: 1.01x slower                                                                                                      |
| regex_compile            | 82.3 ms                                                                                                                | 83.4 ms: 1.01x slower                                                                                                      |
| pickle_pure_python       | 216 us                                                                                                                 | 219 us: 1.01x slower                                                                                                       |
| pycparser                | 728 ms                                                                                                                 | 738 ms: 1.01x slower                                                                                                       |
| logging_simple           | 6.39 us                                                                                                                | 6.48 us: 1.01x slower                                                                                                      |
| chaos                    | 40.2 ms                                                                                                                | 40.8 ms: 1.02x slower                                                                                                      |
| dulwich_log              | 42.1 ms                                                                                                                | 42.9 ms: 1.02x slower                                                                                                      |
| 2to3                     | 220 ms                                                                                                                 | 224 ms: 1.02x slower                                                                                                       |
| sqlglot_v2_normalize     | 73.4 ms                                                                                                                | 74.8 ms: 1.02x slower                                                                                                      |
| generators               | 17.9 ms                                                                                                                | 18.3 ms: 1.02x slower                                                                                                      |
| sphinx                   | 653 ms                                                                                                                 | 667 ms: 1.02x slower                                                                                                       |
| coverage                 | 48.3 ms                                                                                                                | 49.4 ms: 1.02x slower                                                                                                      |
| pylint                   | 200 ms                                                                                                                 | 206 ms: 1.03x slower                                                                                                       |
| richards_super           | 31.5 ms                                                                                                                | 32.4 ms: 1.03x slower                                                                                                      |
| subparsers               | 15.9 ms                                                                                                                | 16.4 ms: 1.03x slower                                                                                                      |
| sympy_sum                | 89.6 ms                                                                                                                | 92.2 ms: 1.03x slower                                                                                                      |
| richards                 | 27.8 ms                                                                                                                | 28.7 ms: 1.03x slower                                                                                                      |
| logging_silent           | 56.3 ns                                                                                                                | 58.1 ns: 1.03x slower                                                                                                      |
| sympy_str                | 175 ms                                                                                                                 | 182 ms: 1.04x slower                                                                                                       |
| genshi_text              | 15.8 ms                                                                                                                | 16.4 ms: 1.04x slower                                                                                                      |
| docutils                 | 1.65 sec                                                                                                               | 1.72 sec: 1.04x slower                                                                                                     |
| unpack_sequence          | 37.0 ns                                                                                                                | 38.5 ns: 1.04x slower                                                                                                      |
| deepcopy                 | 180 us                                                                                                                 | 188 us: 1.04x slower                                                                                                       |
| typing_runtime_protocols | 107 us                                                                                                                 | 112 us: 1.04x slower                                                                                                       |
| sympy_integrate          | 12.9 ms                                                                                                                | 13.5 ms: 1.05x slower                                                                                                      |
| sqlglot_v2_optimize      | 35.1 ms                                                                                                                | 36.9 ms: 1.05x slower                                                                                                      |
| regex_dna                | 114 ms                                                                                                                 | 120 ms: 1.05x slower                                                                                                       |
| float                    | 44.7 ms                                                                                                                | 47.0 ms: 1.05x slower                                                                                                      |
| many_optionals           | 432 us                                                                                                                 | 456 us: 1.05x slower                                                                                                       |
| deepcopy_reduce          | 1.88 us                                                                                                                | 1.99 us: 1.06x slower                                                                                                      |
| comprehensions           | 11.5 us                                                                                                                | 12.2 us: 1.06x slower                                                                                                      |
| regex_v8                 | 13.4 ms                                                                                                                | 14.2 ms: 1.06x slower                                                                                                      |
| go                       | 80.8 ms                                                                                                                | 85.7 ms: 1.06x slower                                                                                                      |
| sympy_expand             | 301 ms                                                                                                                 | 319 ms: 1.06x slower                                                                                                       |
| scimark_sor              | 76.7 ms                                                                                                                | 81.4 ms: 1.06x slower                                                                                                      |
| scimark_monte_carlo      | 43.5 ms                                                                                                                | 46.2 ms: 1.06x slower                                                                                                      |
| unpickle                 | 8.27 us                                                                                                                | 8.80 us: 1.06x slower                                                                                                      |
| regex_effbot             | 1.39 ms                                                                                                                | 1.48 ms: 1.07x slower                                                                                                      |
| genshi_xml               | 34.2 ms                                                                                                                | 36.5 ms: 1.07x slower                                                                                                      |
| sqlglot_v2_parse         | 851 us                                                                                                                 | 910 us: 1.07x slower                                                                                                       |
| sqlglot_v2_transpile     | 1.05 ms                                                                                                                | 1.13 ms: 1.07x slower                                                                                                      |
| spectral_norm            | 55.1 ms                                                                                                                | 59.4 ms: 1.08x slower                                                                                                      |
| async_generators         | 223 ms                                                                                                                 | 244 ms: 1.09x slower                                                                                                       |
| deepcopy_memo            | 19.1 us                                                                                                                | 20.9 us: 1.10x slower                                                                                                      |
| deltablue                | 2.12 ms                                                                                                                | 2.35 ms: 1.11x slower                                                                                                      |
| hexiom                   | 4.12 ms                                                                                                                | 4.73 ms: 1.15x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (23): asyncio_tcp, django_template, python_startup_no_site, python_startup, async_tree_cpu_io_mixed_tg, xml_etree_parse, crypto_pyaes, async_tree_io_tg, json_dumps, pidigits, bench_mp_pool, coroutines, create_gc_cycles, async_tree_cpu_io_mixed, json, async_tree_none, asyncio_tcp_ssl, pathlib, async_tree_memoization_tg, async_tree_io, async_tree_memoization, bench_thread_pool, asyncio_websockets

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 93.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown