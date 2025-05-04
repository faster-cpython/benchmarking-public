# Results vs. base

- fork: python
- ref: 7363e8d24d14abf65163
- machine: windows-amd64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.002x faster
- HPT reliability: 51.39%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.67 sec                                                                                                               | 1.72 sec: 1.03x slower                                                                                                     |
| html5lib       | 38.6 ms                                                                                                                | 39.4 ms: 1.02x slower                                                                                                      |
| sphinx         | 652 ms                                                                                                                 | 662 ms: 1.01x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none  | 182 ms                                                                                                                 | 181 ms: 1.01x faster                                                                                                       |
| coroutines       | 13.7 ms                                                                                                                | 14.3 ms: 1.04x slower                                                                                                      |
| async_generators | 231 ms                                                                                                                 | 247 ms: 1.07x slower                                                                                                       |
| asyncio_tcp_ssl  | 1.34 sec                                                                                                               | 1.47 sec: 1.10x slower                                                                                                     |
| asyncio_tcp      | 423 ms                                                                                                                 | 540 ms: 1.28x slower                                                                                                       |
| Geometric mean   | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

Benchmark hidden because not significant (8): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 63.2 ms                                                                                                                | 56.9 ms: 1.11x faster                                                                                                      |
| float          | 43.9 ms                                                                                                                | 45.3 ms: 1.03x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.02x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 15.1 ms                                                                                                                | 14.4 ms: 1.05x faster                                                                                                      |
| regex_dna      | 120 ms                                                                                                                 | 123 ms: 1.03x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                                                                               | 1.22 sec: 1.14x faster                                                                                                     |
| unpickle_pure_python | 134 us                                                                                                                 | 119 us: 1.12x faster                                                                                                       |
| xml_etree_process    | 40.0 ms                                                                                                                | 36.5 ms: 1.10x faster                                                                                                      |
| xml_etree_generate   | 56.3 ms                                                                                                                | 51.7 ms: 1.09x faster                                                                                                      |
| pickle_dict          | 21.3 us                                                                                                                | 19.7 us: 1.08x faster                                                                                                      |
| pickle_list          | 3.57 us                                                                                                                | 3.38 us: 1.06x faster                                                                                                      |
| unpickle_list        | 2.90 us                                                                                                                | 2.86 us: 1.01x faster                                                                                                      |
| json_dumps           | 6.80 ms                                                                                                                | 6.74 ms: 1.01x faster                                                                                                      |
| xml_etree_parse      | 90.7 ms                                                                                                                | 90.0 ms: 1.01x faster                                                                                                      |
| pickle               | 8.01 us                                                                                                                | 7.97 us: 1.00x faster                                                                                                      |
| pickle_pure_python   | 213 us                                                                                                                 | 215 us: 1.01x slower                                                                                                       |
| json_loads           | 14.6 us                                                                                                                | 14.9 us: 1.02x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 26.4 ms                                                                                                                | 25.7 ms: 1.03x faster                                                                                                      |
| python_startup_no_site | 19.7 ms                                                                                                                | 19.2 ms: 1.02x faster                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.70 ms                                                                                                                | 5.60 ms: 1.20x faster                                                                                                      |
| genshi_xml      | 35.0 ms                                                                                                                | 35.4 ms: 1.01x slower                                                                                                      |
| django_template | 24.3 ms                                                                                                                | 24.7 ms: 1.01x slower                                                                                                      |
| genshi_text     | 15.6 ms                                                                                                                | 16.0 ms: 1.03x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

All benchmarks:
===============

| Benchmark                | results/bm-20250503-3.14.0a7+-7363e8d/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json | results/bm-20250503-3.14.0a7+-7363e8d-JIT/bm-20250503-pythonperf1-amd64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako                     | 6.70 ms                                                                                                                | 5.60 ms: 1.20x faster                                                                                                      |
| tomli_loads              | 1.39 sec                                                                                                               | 1.22 sec: 1.14x faster                                                                                                     |
| scimark_sparse_mat_mult  | 2.61 ms                                                                                                                | 2.30 ms: 1.13x faster                                                                                                      |
| unpickle_pure_python     | 134 us                                                                                                                 | 119 us: 1.12x faster                                                                                                       |
| scimark_fft              | 181 ms                                                                                                                 | 162 ms: 1.12x faster                                                                                                       |
| nbody                    | 63.2 ms                                                                                                                | 56.9 ms: 1.11x faster                                                                                                      |
| bpe_tokeniser            | 2.94 sec                                                                                                               | 2.64 sec: 1.11x faster                                                                                                     |
| xml_etree_process        | 40.0 ms                                                                                                                | 36.5 ms: 1.10x faster                                                                                                      |
| xml_etree_generate       | 56.3 ms                                                                                                                | 51.7 ms: 1.09x faster                                                                                                      |
| pickle_dict              | 21.3 us                                                                                                                | 19.7 us: 1.08x faster                                                                                                      |
| shortest_path            | 384 ms                                                                                                                 | 359 ms: 1.07x faster                                                                                                       |
| pyflate                  | 280 ms                                                                                                                 | 263 ms: 1.06x faster                                                                                                       |
| pickle_list              | 3.57 us                                                                                                                | 3.38 us: 1.06x faster                                                                                                      |
| regex_v8                 | 15.1 ms                                                                                                                | 14.4 ms: 1.05x faster                                                                                                      |
| telco                    | 4.64 ms                                                                                                                | 4.42 ms: 1.05x faster                                                                                                      |
| pprint_pformat           | 1.00 sec                                                                                                               | 957 ms: 1.05x faster                                                                                                       |
| k_core                   | 1.71 sec                                                                                                               | 1.65 sec: 1.04x faster                                                                                                     |
| python_startup           | 26.4 ms                                                                                                                | 25.7 ms: 1.03x faster                                                                                                      |
| python_startup_no_site   | 19.7 ms                                                                                                                | 19.2 ms: 1.02x faster                                                                                                      |
| crypto_pyaes             | 47.8 ms                                                                                                                | 46.6 ms: 1.02x faster                                                                                                      |
| sqlglot_v2_parse         | 830 us                                                                                                                 | 812 us: 1.02x faster                                                                                                       |
| fannkuch                 | 254 ms                                                                                                                 | 249 ms: 1.02x faster                                                                                                       |
| pprint_safe_repr         | 496 ms                                                                                                                 | 486 ms: 1.02x faster                                                                                                       |
| logging_format           | 6.87 us                                                                                                                | 6.75 us: 1.02x faster                                                                                                      |
| logging_simple           | 6.40 us                                                                                                                | 6.29 us: 1.02x faster                                                                                                      |
| connected_components     | 334 ms                                                                                                                 | 328 ms: 1.02x faster                                                                                                       |
| sqlite_synth             | 1.58 us                                                                                                                | 1.56 us: 1.01x faster                                                                                                      |
| unpickle_list            | 2.90 us                                                                                                                | 2.86 us: 1.01x faster                                                                                                      |
| raytrace                 | 182 ms                                                                                                                 | 179 ms: 1.01x faster                                                                                                       |
| subparsers               | 17.0 ms                                                                                                                | 16.7 ms: 1.01x faster                                                                                                      |
| async_tree_none          | 182 ms                                                                                                                 | 181 ms: 1.01x faster                                                                                                       |
| json_dumps               | 6.80 ms                                                                                                                | 6.74 ms: 1.01x faster                                                                                                      |
| xml_etree_parse          | 90.7 ms                                                                                                                | 90.0 ms: 1.01x faster                                                                                                      |
| pickle                   | 8.01 us                                                                                                                | 7.97 us: 1.00x faster                                                                                                      |
| pickle_pure_python       | 213 us                                                                                                                 | 215 us: 1.01x slower                                                                                                       |
| genshi_xml               | 35.0 ms                                                                                                                | 35.4 ms: 1.01x slower                                                                                                      |
| nqueens                  | 60.9 ms                                                                                                                | 61.6 ms: 1.01x slower                                                                                                      |
| sympy_sum                | 88.1 ms                                                                                                                | 89.2 ms: 1.01x slower                                                                                                      |
| django_template          | 24.3 ms                                                                                                                | 24.7 ms: 1.01x slower                                                                                                      |
| sphinx                   | 652 ms                                                                                                                 | 662 ms: 1.01x slower                                                                                                       |
| sympy_str                | 172 ms                                                                                                                 | 175 ms: 1.02x slower                                                                                                       |
| json_loads               | 14.6 us                                                                                                                | 14.9 us: 1.02x slower                                                                                                      |
| html5lib                 | 38.6 ms                                                                                                                | 39.4 ms: 1.02x slower                                                                                                      |
| sympy_expand             | 297 ms                                                                                                                 | 304 ms: 1.02x slower                                                                                                       |
| deltablue                | 2.16 ms                                                                                                                | 2.21 ms: 1.02x slower                                                                                                      |
| richards                 | 27.8 ms                                                                                                                | 28.4 ms: 1.02x slower                                                                                                      |
| generators               | 19.5 ms                                                                                                                | 19.9 ms: 1.02x slower                                                                                                      |
| logging_silent           | 56.2 ns                                                                                                                | 57.7 ns: 1.03x slower                                                                                                      |
| deepcopy                 | 177 us                                                                                                                 | 181 us: 1.03x slower                                                                                                       |
| sympy_integrate          | 12.6 ms                                                                                                                | 12.9 ms: 1.03x slower                                                                                                      |
| genshi_text              | 15.6 ms                                                                                                                | 16.0 ms: 1.03x slower                                                                                                      |
| docutils                 | 1.67 sec                                                                                                               | 1.72 sec: 1.03x slower                                                                                                     |
| float                    | 43.9 ms                                                                                                                | 45.3 ms: 1.03x slower                                                                                                      |
| mdp                      | 791 ms                                                                                                                 | 817 ms: 1.03x slower                                                                                                       |
| regex_dna                | 120 ms                                                                                                                 | 123 ms: 1.03x slower                                                                                                       |
| deepcopy_reduce          | 1.86 us                                                                                                                | 1.92 us: 1.03x slower                                                                                                      |
| richards_super           | 31.1 ms                                                                                                                | 32.2 ms: 1.03x slower                                                                                                      |
| sqlglot_v2_normalize     | 71.5 ms                                                                                                                | 74.0 ms: 1.04x slower                                                                                                      |
| go                       | 77.9 ms                                                                                                                | 80.7 ms: 1.04x slower                                                                                                      |
| pycparser                | 712 ms                                                                                                                 | 739 ms: 1.04x slower                                                                                                       |
| chaos                    | 38.4 ms                                                                                                                | 39.8 ms: 1.04x slower                                                                                                      |
| meteor_contest           | 74.3 ms                                                                                                                | 77.3 ms: 1.04x slower                                                                                                      |
| coroutines               | 13.7 ms                                                                                                                | 14.3 ms: 1.04x slower                                                                                                      |
| many_optionals           | 440 us                                                                                                                 | 460 us: 1.04x slower                                                                                                       |
| typing_runtime_protocols | 109 us                                                                                                                 | 114 us: 1.05x slower                                                                                                       |
| sqlglot_v2_optimize      | 34.2 ms                                                                                                                | 35.8 ms: 1.05x slower                                                                                                      |
| comprehensions           | 11.4 us                                                                                                                | 11.9 us: 1.05x slower                                                                                                      |
| scimark_sor              | 75.1 ms                                                                                                                | 79.0 ms: 1.05x slower                                                                                                      |
| scimark_monte_carlo      | 40.4 ms                                                                                                                | 42.7 ms: 1.06x slower                                                                                                      |
| scimark_lu               | 56.5 ms                                                                                                                | 59.9 ms: 1.06x slower                                                                                                      |
| async_generators         | 231 ms                                                                                                                 | 247 ms: 1.07x slower                                                                                                       |
| asyncio_tcp_ssl          | 1.34 sec                                                                                                               | 1.47 sec: 1.10x slower                                                                                                     |
| hexiom                   | 4.03 ms                                                                                                                | 4.44 ms: 1.10x slower                                                                                                      |
| spectral_norm            | 56.3 ms                                                                                                                | 63.6 ms: 1.13x slower                                                                                                      |
| deepcopy_memo            | 18.5 us                                                                                                                | 21.6 us: 1.17x slower                                                                                                      |
| unpack_sequence          | 33.3 ns                                                                                                                | 40.9 ns: 1.23x slower                                                                                                      |
| asyncio_tcp              | 423 ms                                                                                                                 | 540 ms: 1.28x slower                                                                                                       |
| Geometric mean           | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (24): asyncio_websockets, bench_thread_pool, pathlib, async_tree_cpu_io_mixed_tg, create_gc_cycles, async_tree_cpu_io_mixed, bench_mp_pool, async_tree_none_tg, coverage, gc_traversal, xml_etree_iterparse, async_tree_memoization_tg, sqlglot_v2_transpile, pidigits, async_tree_memoization, regex_compile, async_tree_io_tg, 2to3, json, regex_effbot, async_tree_io, unpickle, pylint, dulwich_log

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 51.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown