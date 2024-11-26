# Results vs. base

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-amd64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.040x faster
- HPT reliability: 94.22%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 225 ms                                                                                                                 | 246 ms: 1.09x slower                                                                                                       |
| docutils       | 1.69 sec                                                                                                               | 1.89 sec: 1.12x slower                                                                                                     |
| html5lib       | 40.0 ms                                                                                                                | 38.6 ms: 1.04x faster                                                                                                      |
| sphinx         | 670 ms                                                                                                                 | 766 ms: 1.14x slower                                                                                                       |
| tornado_http   | 93.4 ms                                                                                                                | 97.1 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.07x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|-------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization  | 278 ms                                                                                                                 | 264 ms: 1.05x faster                                                                                                       |
| async_tree_none         | 220 ms                                                                                                                 | 209 ms: 1.05x faster                                                                                                       |
| async_tree_io           | 566 ms                                                                                                                 | 555 ms: 1.02x faster                                                                                                       |
| async_tree_cpu_io_mixed | 382 ms                                                                                                                 | 391 ms: 1.02x slower                                                                                                       |
| async_tree_none_tg      | 211 ms                                                                                                                 | 219 ms: 1.04x slower                                                                                                       |
| asyncio_websockets      | 304 ms                                                                                                                 | 318 ms: 1.05x slower                                                                                                       |
| coroutines              | 13.5 ms                                                                                                                | 14.2 ms: 1.05x slower                                                                                                      |
| async_generators        | 243 ms                                                                                                                 | 268 ms: 1.11x slower                                                                                                       |
| Geometric mean          | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 79.4 ms                                                                                                                | 54.0 ms: 1.47x faster                                                                                                      |
| float          | 54.9 ms                                                                                                                | 46.4 ms: 1.18x faster                                                                                                      |
| pidigits       | 147 ms                                                                                                                 | 147 ms: 1.00x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.20x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 92.2 ms                                                                                                                | 90.8 ms: 1.02x faster                                                                                                      |
| regex_v8       | 14.6 ms                                                                                                                | 14.8 ms: 1.01x slower                                                                                                      |
| regex_dna      | 113 ms                                                                                                                 | 115 ms: 1.01x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.59 sec                                                                                                               | 1.28 sec: 1.25x faster                                                                                                     |
| xml_etree_generate   | 59.4 ms                                                                                                                | 50.2 ms: 1.18x faster                                                                                                      |
| xml_etree_process    | 41.2 ms                                                                                                                | 35.6 ms: 1.16x faster                                                                                                      |
| pickle_pure_python   | 228 us                                                                                                                 | 206 us: 1.11x faster                                                                                                       |
| json_dumps           | 6.73 ms                                                                                                                | 6.12 ms: 1.10x faster                                                                                                      |
| unpickle_pure_python | 159 us                                                                                                                 | 145 us: 1.10x faster                                                                                                       |
| xml_etree_iterparse  | 67.6 ms                                                                                                                | 62.8 ms: 1.08x faster                                                                                                      |
| xml_etree_parse      | 95.5 ms                                                                                                                | 92.7 ms: 1.03x faster                                                                                                      |
| json_loads           | 14.4 us                                                                                                                | 14.5 us: 1.00x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.11x faster                                                                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 23.8 ms                                                                                                                | 24.1 ms: 1.01x slower                                                                                                      |
| python_startup_no_site | 17.8 ms                                                                                                                | 18.1 ms: 1.01x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.95 ms                                                                                                                | 4.97 ms: 1.40x faster                                                                                                      |
| django_template | 24.9 ms                                                                                                                | 26.9 ms: 1.08x slower                                                                                                      |
| genshi_text     | 17.6 ms                                                                                                                | 19.2 ms: 1.09x slower                                                                                                      |
| genshi_xml      | 36.6 ms                                                                                                                | 46.9 ms: 1.28x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                | results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json | results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-pythonperf1-amd64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                    | 79.4 ms                                                                                                                | 54.0 ms: 1.47x faster                                                                                                      |
| scimark_sor              | 93.0 ms                                                                                                                | 63.5 ms: 1.46x faster                                                                                                      |
| mako                     | 6.95 ms                                                                                                                | 4.97 ms: 1.40x faster                                                                                                      |
| spectral_norm            | 71.6 ms                                                                                                                | 52.8 ms: 1.35x faster                                                                                                      |
| scimark_monte_carlo      | 49.9 ms                                                                                                                | 36.9 ms: 1.35x faster                                                                                                      |
| scimark_fft              | 206 ms                                                                                                                 | 154 ms: 1.34x faster                                                                                                       |
| deepcopy_memo            | 21.5 us                                                                                                                | 16.2 us: 1.32x faster                                                                                                      |
| tomli_loads              | 1.59 sec                                                                                                               | 1.28 sec: 1.25x faster                                                                                                     |
| pprint_pformat           | 1.12 sec                                                                                                               | 915 ms: 1.22x faster                                                                                                       |
| scimark_sparse_mat_mult  | 2.68 ms                                                                                                                | 2.20 ms: 1.22x faster                                                                                                      |
| pprint_safe_repr         | 551 ms                                                                                                                 | 453 ms: 1.22x faster                                                                                                       |
| scimark_lu               | 64.5 ms                                                                                                                | 53.4 ms: 1.21x faster                                                                                                      |
| crypto_pyaes             | 48.6 ms                                                                                                                | 40.7 ms: 1.19x faster                                                                                                      |
| xml_etree_generate       | 59.4 ms                                                                                                                | 50.2 ms: 1.18x faster                                                                                                      |
| float                    | 54.9 ms                                                                                                                | 46.4 ms: 1.18x faster                                                                                                      |
| logging_silent           | 65.6 ns                                                                                                                | 55.8 ns: 1.18x faster                                                                                                      |
| bpe_tokeniser            | 3.14 sec                                                                                                               | 2.68 sec: 1.17x faster                                                                                                     |
| fannkuch                 | 289 ms                                                                                                                 | 247 ms: 1.17x faster                                                                                                       |
| xml_etree_process        | 41.2 ms                                                                                                                | 35.6 ms: 1.16x faster                                                                                                      |
| pickle_pure_python       | 228 us                                                                                                                 | 206 us: 1.11x faster                                                                                                       |
| telco                    | 4.84 ms                                                                                                                | 4.40 ms: 1.10x faster                                                                                                      |
| json_dumps               | 6.73 ms                                                                                                                | 6.12 ms: 1.10x faster                                                                                                      |
| unpickle_pure_python     | 159 us                                                                                                                 | 145 us: 1.10x faster                                                                                                       |
| pyflate                  | 324 ms                                                                                                                 | 298 ms: 1.09x faster                                                                                                       |
| chaos                    | 44.3 ms                                                                                                                | 41.1 ms: 1.08x faster                                                                                                      |
| dulwich_log              | 43.0 ms                                                                                                                | 39.9 ms: 1.08x faster                                                                                                      |
| xml_etree_iterparse      | 67.6 ms                                                                                                                | 62.8 ms: 1.08x faster                                                                                                      |
| connected_components     | 328 ms                                                                                                                 | 307 ms: 1.07x faster                                                                                                       |
| meteor_contest           | 77.5 ms                                                                                                                | 72.7 ms: 1.07x faster                                                                                                      |
| logging_format           | 6.97 us                                                                                                                | 6.56 us: 1.06x faster                                                                                                      |
| deepcopy_reduce          | 1.95 us                                                                                                                | 1.85 us: 1.06x faster                                                                                                      |
| logging_simple           | 6.50 us                                                                                                                | 6.16 us: 1.05x faster                                                                                                      |
| async_tree_memoization   | 278 ms                                                                                                                 | 264 ms: 1.05x faster                                                                                                       |
| async_tree_none          | 220 ms                                                                                                                 | 209 ms: 1.05x faster                                                                                                       |
| shortest_path            | 360 ms                                                                                                                 | 342 ms: 1.05x faster                                                                                                       |
| sqlglot_parse            | 938 us                                                                                                                 | 893 us: 1.05x faster                                                                                                       |
| html5lib                 | 40.0 ms                                                                                                                | 38.6 ms: 1.04x faster                                                                                                      |
| sqlite_synth             | 1.63 us                                                                                                                | 1.57 us: 1.04x faster                                                                                                      |
| k_core                   | 2.52 sec                                                                                                               | 2.43 sec: 1.04x faster                                                                                                     |
| xml_etree_parse          | 95.5 ms                                                                                                                | 92.7 ms: 1.03x faster                                                                                                      |
| comprehensions           | 12.1 us                                                                                                                | 11.8 us: 1.03x faster                                                                                                      |
| async_tree_io            | 566 ms                                                                                                                 | 555 ms: 1.02x faster                                                                                                       |
| pycparser                | 734 ms                                                                                                                 | 722 ms: 1.02x faster                                                                                                       |
| regex_compile            | 92.2 ms                                                                                                                | 90.8 ms: 1.02x faster                                                                                                      |
| json                     | 3.04 ms                                                                                                                | 3.00 ms: 1.01x faster                                                                                                      |
| deepcopy                 | 192 us                                                                                                                 | 190 us: 1.01x faster                                                                                                       |
| coverage                 | 46.7 ms                                                                                                                | 46.4 ms: 1.01x faster                                                                                                      |
| pidigits                 | 147 ms                                                                                                                 | 147 ms: 1.00x faster                                                                                                       |
| mdp                      | 1.51 sec                                                                                                               | 1.52 sec: 1.00x slower                                                                                                     |
| json_loads               | 14.4 us                                                                                                                | 14.5 us: 1.00x slower                                                                                                      |
| generators               | 22.5 ms                                                                                                                | 22.7 ms: 1.01x slower                                                                                                      |
| python_startup           | 23.8 ms                                                                                                                | 24.1 ms: 1.01x slower                                                                                                      |
| regex_v8                 | 14.6 ms                                                                                                                | 14.8 ms: 1.01x slower                                                                                                      |
| deltablue                | 2.34 ms                                                                                                                | 2.37 ms: 1.01x slower                                                                                                      |
| python_startup_no_site   | 17.8 ms                                                                                                                | 18.1 ms: 1.01x slower                                                                                                      |
| regex_dna                | 113 ms                                                                                                                 | 115 ms: 1.01x slower                                                                                                       |
| sqlglot_transpile        | 1.16 ms                                                                                                                | 1.18 ms: 1.02x slower                                                                                                      |
| nqueens                  | 64.3 ms                                                                                                                | 65.5 ms: 1.02x slower                                                                                                      |
| richards                 | 34.0 ms                                                                                                                | 34.6 ms: 1.02x slower                                                                                                      |
| go                       | 90.1 ms                                                                                                                | 91.9 ms: 1.02x slower                                                                                                      |
| thrift                   | 531 us                                                                                                                 | 542 us: 1.02x slower                                                                                                       |
| async_tree_cpu_io_mixed  | 382 ms                                                                                                                 | 391 ms: 1.02x slower                                                                                                       |
| tornado_http             | 93.4 ms                                                                                                                | 97.1 ms: 1.04x slower                                                                                                      |
| async_tree_none_tg       | 211 ms                                                                                                                 | 219 ms: 1.04x slower                                                                                                       |
| asyncio_websockets       | 304 ms                                                                                                                 | 318 ms: 1.05x slower                                                                                                       |
| coroutines               | 13.5 ms                                                                                                                | 14.2 ms: 1.05x slower                                                                                                      |
| typing_runtime_protocols | 111 us                                                                                                                 | 117 us: 1.06x slower                                                                                                       |
| sympy_expand             | 306 ms                                                                                                                 | 323 ms: 1.06x slower                                                                                                       |
| sqlglot_normalize        | 198 ms                                                                                                                 | 210 ms: 1.06x slower                                                                                                       |
| bench_mp_pool            | 83.1 ms                                                                                                                | 88.5 ms: 1.07x slower                                                                                                      |
| sympy_str                | 178 ms                                                                                                                 | 192 ms: 1.08x slower                                                                                                       |
| django_template          | 24.9 ms                                                                                                                | 26.9 ms: 1.08x slower                                                                                                      |
| pylint                   | 224 ms                                                                                                                 | 244 ms: 1.09x slower                                                                                                       |
| raytrace                 | 199 ms                                                                                                                 | 216 ms: 1.09x slower                                                                                                       |
| genshi_text              | 17.6 ms                                                                                                                | 19.2 ms: 1.09x slower                                                                                                      |
| 2to3                     | 225 ms                                                                                                                 | 246 ms: 1.09x slower                                                                                                       |
| async_generators         | 243 ms                                                                                                                 | 268 ms: 1.11x slower                                                                                                       |
| hexiom                   | 4.60 ms                                                                                                                | 5.14 ms: 1.12x slower                                                                                                      |
| docutils                 | 1.69 sec                                                                                                               | 1.89 sec: 1.12x slower                                                                                                     |
| sympy_sum                | 90.2 ms                                                                                                                | 102 ms: 1.13x slower                                                                                                       |
| sphinx                   | 670 ms                                                                                                                 | 766 ms: 1.14x slower                                                                                                       |
| sqlglot_optimize         | 37.3 ms                                                                                                                | 42.7 ms: 1.14x slower                                                                                                      |
| sympy_integrate          | 13.5 ms                                                                                                                | 15.6 ms: 1.16x slower                                                                                                      |
| genshi_xml               | 36.6 ms                                                                                                                | 46.9 ms: 1.28x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmark hidden because not significant (9): async_tree_io_tg, pathlib, gc_traversal, async_tree_cpu_io_mixed_tg, bench_thread_pool, regex_effbot, richards_super, create_gc_cycles, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.040x faster
# HPT report

- Reliability score: 94.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown