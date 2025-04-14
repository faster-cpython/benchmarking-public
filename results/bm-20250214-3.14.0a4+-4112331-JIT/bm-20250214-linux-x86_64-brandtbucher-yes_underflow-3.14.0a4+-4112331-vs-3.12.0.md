# Results vs. 3.12.0

- fork: brandtbucher
- ref: yes_underflow
- machine: linux-x86_64
- commit hash: 4112331
- commit date: 2025-02-14
- overall geometric mean: 1.078x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                  |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 633 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 329 ms: 1.75x faster                                                  |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.0 ms: 1.28x faster                                                 |
| nbody          | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.05 ms: 1.18x faster                                                 |
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                  |
| regex_dna      | 212 ms                                                 | 202 ms: 1.05x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 202 us: 1.14x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.9 us: 1.02x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.95 ms: 1.20x faster                                                 |
| django_template | 34.6 ms                                                | 35.7 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 609 ms: 1.94x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 633 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 329 ms: 1.75x faster                                                  |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.51x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                 |
| deepcopy                   | 371 us                                                 | 274 us: 1.35x faster                                                  |
| float                      | 84.7 ms                                                | 66.0 ms: 1.28x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                 |
| spectral_norm              | 115 ms                                                 | 93.0 ms: 1.23x faster                                                 |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.23x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.79 us: 1.20x faster                                                 |
| mako                       | 11.9 ms                                                | 9.95 ms: 1.20x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 63.4 ms: 1.18x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.05 ms: 1.18x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 70.8 ms: 1.16x faster                                                 |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 202 us: 1.14x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.45 ms: 1.14x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                 |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                 |
| nbody                      | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                 |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                  |
| raytrace                   | 312 ms                                                 | 289 ms: 1.08x faster                                                  |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                  |
| logging_format             | 7.23 us                                                | 6.83 us: 1.06x faster                                                 |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                 |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                  |
| regex_dna                  | 212 ms                                                 | 202 ms: 1.05x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                 |
| logging_simple             | 6.46 us                                                | 6.27 us: 1.03x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.03x faster                                                |
| pyflate                    | 482 ms                                                 | 471 ms: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                  |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.59 sec: 1.01x slower                                                |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                  |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.02x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 70.5 ms: 1.03x slower                                                 |
| django_template            | 34.6 ms                                                | 35.7 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                 |
| nqueens                    | 83.3 ms                                                | 87.9 ms: 1.05x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 890 us: 1.06x slower                                                  |
| telco                      | 7.10 ms                                                | 7.67 ms: 1.08x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                 |
| deltablue                  | 3.72 ms                                                | 4.22 ms: 1.13x slower                                                 |
| hexiom                     | 6.41 ms                                                | 7.68 ms: 1.20x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.65 ms: 1.22x slower                                                 |
| coverage                   | 72.7 ms                                                | 90.3 ms: 1.24x slower                                                 |
| logging_silent             | 104 ns                                                 | 134 ns: 1.28x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                 |
| richards                   | 45.8 ms                                                | 64.2 ms: 1.40x slower                                                 |
| richards_super             | 51.5 ms                                                | 75.9 ms: 1.47x slower                                                 |
| generators                 | 31.2 ms                                                | 49.5 ms: 1.59x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.37x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (4): pprint_safe_repr, json, sqlglot_optimize, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250214-3.14.0a4+-4112331-JIT/bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x