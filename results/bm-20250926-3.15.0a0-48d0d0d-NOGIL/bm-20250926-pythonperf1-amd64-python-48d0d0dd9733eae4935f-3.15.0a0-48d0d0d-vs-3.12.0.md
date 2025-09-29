# Results vs. 3.12.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.027x faster
- HPT reliability: 89.58%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.66 sec                                                    | 2.81 sec: 1.69x slower                                                     |
| Geometric mean | (ref)                                                       | 1.30x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 317 ms: 2.43x faster                                                       |
| async_tree_io              | 731 ms                                                      | 339 ms: 2.16x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.96x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 188 ms: 1.96x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 307 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.86x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 137 ms: 1.11x faster                                                       |
| nbody          | 71.9 ms                                                     | 78.5 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.65 ms: 1.02x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 90.6 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 57.3 ms: 1.14x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                      |
| pickle               | 7.43 us                                                     | 7.84 us: 1.05x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.06 ms: 1.06x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.02 us: 1.07x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 60.6 ms: 1.09x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.0 us: 1.09x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.12x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 3.12 us: 1.13x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 223 us: 1.14x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 43.2 ms: 1.15x slower                                                      |
| json_loads           | 13.9 us                                                     | 16.5 us: 1.18x slower                                                      |
| unpickle             | 8.18 us                                                     | 10.3 us: 1.26x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                      |
| mako            | 7.09 ms                                                     | 9.65 ms: 1.36x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.24x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.7 ms: 2.80x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 317 ms: 2.43x faster                                                       |
| async_tree_io              | 731 ms                                                      | 339 ms: 2.16x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 145 ms: 1.96x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 188 ms: 1.96x faster                                                       |
| async_tree_none            | 291 ms                                                      | 168 ms: 1.73x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 204 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 307 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.33 us: 1.33x faster                                                      |
| deepcopy                   | 238 us                                                      | 182 us: 1.31x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.06 sec: 1.29x faster                                                     |
| float                      | 56.8 ms                                                     | 45.1 ms: 1.26x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.8 us: 1.26x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.3 us: 1.25x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.23 ms: 1.24x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 57.3 ms: 1.14x faster                                                      |
| pidigits                   | 152 ms                                                      | 137 ms: 1.11x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 33.8 ns: 1.11x faster                                                      |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                       |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.3 ms: 1.07x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.4 ms: 1.07x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.99 us: 1.05x faster                                                      |
| go                         | 91.6 ms                                                     | 88.5 ms: 1.03x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.7 ms: 1.03x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| pycparser                  | 699 ms                                                      | 692 ms: 1.01x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 60.0 ns: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.37 us: 1.01x slower                                                      |
| scimark_fft                | 184 ms                                                      | 188 ms: 1.02x slower                                                       |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.65 ms: 1.02x slower                                                      |
| pyflate                    | 295 ms                                                      | 302 ms: 1.02x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 94.1 ms: 1.03x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 90.6 ms: 1.04x slower                                                      |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.04x slower                                                       |
| chaos                      | 43.3 ms                                                     | 45.1 ms: 1.04x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 82.2 ms: 1.04x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 540 ms: 1.05x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 70.5 ms: 1.05x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.84 us: 1.05x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.10 us: 1.06x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.06x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.06 ms: 1.06x slower                                                      |
| async_generators           | 239 ms                                                      | 255 ms: 1.06x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.02 us: 1.07x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 63.5 ms: 1.08x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 74.7 ms: 1.08x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.45 ms: 1.08x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 60.6 ms: 1.09x slower                                                      |
| raytrace                   | 192 ms                                                      | 210 ms: 1.09x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.0 us: 1.09x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.36 ms: 1.09x slower                                                      |
| nbody                      | 71.9 ms                                                     | 78.5 ms: 1.09x slower                                                      |
| sympy_expand               | 284 ms                                                      | 311 ms: 1.10x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 540 ms: 1.11x slower                                                       |
| richards                   | 28.4 ms                                                     | 31.6 ms: 1.11x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.9 ms: 1.12x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.12x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.12 us: 1.13x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 71.4 ms: 1.14x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 223 us: 1.14x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 43.2 ms: 1.15x slower                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.40 sec: 1.15x slower                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.94 ms: 1.15x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 85.8 ms: 1.15x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.9 ms: 1.15x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 56.5 ms: 1.17x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.0 ms: 1.17x slower                                                      |
| json_loads                 | 13.9 us                                                     | 16.5 us: 1.18x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.00 ms: 1.21x slower                                                      |
| fannkuch                   | 247 ms                                                      | 302 ms: 1.22x slower                                                       |
| bench_thread_pool          | 857 us                                                      | 1.05 ms: 1.23x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.3 us: 1.26x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.00 ms: 1.33x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 128 us: 1.35x slower                                                       |
| mako                       | 7.09 ms                                                     | 9.65 ms: 1.36x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.61 sec: 1.54x slower                                                     |
| coverage                   | 40.8 ms                                                     | 66.8 ms: 1.64x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.31 sec: 1.69x slower                                                     |
| docutils                   | 1.66 sec                                                    | 2.81 sec: 1.69x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): 2to3
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250926-3.15.0a0-48d0d0d-NOGIL/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 89.58% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown