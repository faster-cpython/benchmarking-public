# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_4096
- machine: linux-x86_64
- commit hash: a2be6fd
- commit date: 2024-11-11
- overall geometric mean: 1.070x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                |
| docutils       | 2.77 sec                                               | 2.89 sec: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                                |
| async_tree_io              | 1.16 sec                                               | 860 ms: 1.34x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 980 ms: 1.21x faster                                                |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 83.4 ms: 1.16x faster                                               |
| float          | 84.7 ms                                                | 76.3 ms: 1.11x faster                                               |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                |
| regex_dna      | 212 ms                                                 | 211 ms: 1.00x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.62 ms: 1.00x slower                                               |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                              |
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 81.7 ms: 1.09x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 56.9 ms: 1.08x faster                                               |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 157 ms: 1.02x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                               |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                               |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.15x faster                                               |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 321 ms: 1.40x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.40x faster                                                |
| deepcopy                   | 371 us                                                 | 268 us: 1.39x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                               |
| async_tree_io              | 1.16 sec                                               | 860 ms: 1.34x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 551 ms: 1.32x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                |
| comprehensions             | 21.8 us                                                | 17.5 us: 1.25x faster                                               |
| richards                   | 45.8 ms                                                | 37.3 ms: 1.23x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                               |
| richards_super             | 51.5 ms                                                | 42.2 ms: 1.22x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 980 ms: 1.21x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 68.3 ms: 1.20x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                                |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.19x faster                                                |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 64.4 ms: 1.17x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                               |
| nbody                      | 97.0 ms                                                | 83.4 ms: 1.16x faster                                               |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.15x faster                                               |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                               |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                               |
| float                      | 84.7 ms                                                | 76.3 ms: 1.11x faster                                               |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 81.7 ms: 1.09x faster                                               |
| fannkuch                   | 417 ms                                                 | 383 ms: 1.09x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.9 ms: 1.08x faster                                               |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.07x faster                                               |
| json                       | 5.26 ms                                                | 4.90 ms: 1.07x faster                                               |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.73 ms: 1.07x faster                                               |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                                |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                |
| sympy_sum                  | 169 ms                                                 | 159 ms: 1.06x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                              |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                               |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                               |
| sympy_str                  | 300 ms                                                 | 292 ms: 1.03x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 21.0 ms: 1.02x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 157 ms: 1.02x faster                                                |
| async_generators           | 463 ms                                                 | 456 ms: 1.01x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                               |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                               |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.00x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.62 ms: 1.00x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 55.4 ms: 1.01x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                               |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                |
| bench_thread_pool          | 842 us                                                 | 869 us: 1.03x slower                                                |
| docutils                   | 2.77 sec                                               | 2.89 sec: 1.04x slower                                              |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.04x slower                                              |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                               |
| nqueens                    | 83.3 ms                                                | 87.1 ms: 1.05x slower                                               |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                               |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.07x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                               |
| hexiom                     | 6.41 ms                                                | 7.10 ms: 1.11x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.36 ms: 1.15x slower                                               |
| generators                 | 31.2 ms                                                | 36.0 ms: 1.15x slower                                               |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                               |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 78.4 ms: 3.27x slower                                               |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (4): sqlglot_normalize, pickle_pure_python, pycparser, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241111-3.14.0a1+-a2be6fd-JIT/bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.070x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.10x