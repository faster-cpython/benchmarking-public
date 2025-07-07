# Results vs. 3.12.0

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.72x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.3 ms: 1.38x faster                                                      |
| float          | 56.8 ms                                                     | 42.8 ms: 1.33x faster                                                      |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.6 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 106 us: 1.25x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.2 ms: 1.07x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                      |
| pickle               | 7.43 us                                                     | 7.55 us: 1.02x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 203 us: 1.04x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.3 us: 1.05x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.73 us: 1.07x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.11 ms: 1.07x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.30 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.44 ms: 1.30x faster                                                      |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.9 ms: 2.53x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 385 ms: 2.00x faster                                                       |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.74x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 165 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 798 ms: 1.72x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 205 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 337 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.45x faster                                                     |
| deepcopy                   | 238 us                                                      | 168 us: 1.42x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.3 ms: 1.38x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.5 us: 1.34x faster                                                      |
| float                      | 56.8 ms                                                     | 42.8 ms: 1.33x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.44 ms: 1.30x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 106 us: 1.25x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.9 us: 1.25x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                     |
| scimark_fft                | 184 ms                                                      | 151 ms: 1.22x faster                                                       |
| go                         | 91.6 ms                                                     | 75.0 ms: 1.22x faster                                                      |
| pyflate                    | 295 ms                                                      | 252 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.15x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 449 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.27 ms: 1.13x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 927 ms: 1.13x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 54.2 ns: 1.12x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.6 ms: 1.11x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                      |
| fannkuch                   | 247 ms                                                      | 224 ms: 1.10x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.5 ms: 1.10x faster                                                      |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.8 ms: 1.08x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 62.1 ms: 1.08x faster                                                      |
| richards                   | 28.4 ms                                                     | 26.4 ms: 1.07x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.2 ms: 1.07x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 86.8 ms: 1.07x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.65 us: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.3 ms: 1.06x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.3 ms: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 59.6 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.0 ms: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.2 ms: 1.05x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 46.3 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.5 ms: 1.05x faster                                                      |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.8 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.03x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 36.5 ns: 1.03x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.12 us: 1.03x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.61 us: 1.02x faster                                                      |
| deltablue                  | 2.16 ms                                                     | 2.13 ms: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.06 ms: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| regex_v8                   | 14.2 ms                                                     | 14.2 ms: 1.01x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.55 us: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                       |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.83 us: 1.03x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.25 ms: 1.03x slower                                                      |
| sympy_expand               | 284 ms                                                      | 292 ms: 1.03x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.7 ms: 1.03x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 203 us: 1.04x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.3 us: 1.05x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.07x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.73 us: 1.07x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.11 ms: 1.07x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 528 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.09x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.30 us: 1.17x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.6 ms: 1.26x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.8 ms: 1.33x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 95.3 ms: 1.38x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.16 ms: 1.42x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.32 ms: 1.75x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (3): bench_thread_pool, pycparser, 2to3
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.123x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown