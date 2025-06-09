# Results vs. 3.12.0

- fork: python
- ref: aac22ea212849f8fffee
- machine: windows-amd64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.057x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                       |
| async_tree_io              | 731 ms                                                      | 402 ms: 1.82x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 212 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.66x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                      |
| nbody          | 71.9 ms                                                     | 64.8 ms: 1.11x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.0 ms: 1.02x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 137 us: 1.03x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.33 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                      |
| django_template | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.2 ms: 2.50x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                       |
| async_tree_io              | 731 ms                                                      | 402 ms: 1.82x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                       |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.68x faster                                                       |
| mdp                        | 1.37 sec                                                    | 815 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 212 ms: 1.60x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 331 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                       |
| deepcopy                   | 238 us                                                      | 172 us: 1.39x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.3 us: 1.30x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.28x faster                                                      |
| float                      | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                      |
| go                         | 91.6 ms                                                     | 77.0 ms: 1.19x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 57.5 ms: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                      |
| nbody                      | 71.9 ms                                                     | 64.8 ms: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 80.5 ms: 1.09x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.0 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.4 ms: 1.08x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                                      |
| scimark_fft                | 184 ms                                                      | 173 ms: 1.07x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 74.5 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                       |
| raytrace                   | 192 ms                                                      | 183 ms: 1.05x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.79 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.1 ms: 1.04x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                      |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.03x faster                                                       |
| async_generators           | 239 ms                                                      | 233 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.3 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.9 ms: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.4 ms: 1.02x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.8 ms: 1.02x faster                                                      |
| pyflate                    | 295 ms                                                      | 289 ms: 1.02x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.04 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.54 ms: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.33 us: 1.01x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| logging_format             | 6.72 us                                                     | 6.81 us: 1.01x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.0 ms: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| fannkuch                   | 247 ms                                                      | 253 ms: 1.03x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 137 us: 1.03x slower                                                       |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| pycparser                  | 699 ms                                                      | 720 ms: 1.03x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.05x slower                                                     |
| pprint_safe_repr           | 513 ms                                                      | 541 ms: 1.05x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.2 ms: 1.06x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.33 ms: 1.11x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.12x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.71 ms: 1.14x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.40x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.76x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 315 ns: 5.21x slower                                                       |
| coverage                   | 40.8 ms                                                     | 299 ms: 7.32x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (4): coroutines, scimark_lu, json, xml_etree_iterparse
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-pythonperf1-amd64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown