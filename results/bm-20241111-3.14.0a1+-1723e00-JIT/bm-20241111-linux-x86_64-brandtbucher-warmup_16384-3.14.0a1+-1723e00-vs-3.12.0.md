# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_16384
- machine: linux-x86_64
- commit hash: 1723e00
- commit date: 2024-11-11
- overall geometric mean: 1.067x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                 |
| docutils       | 2.77 sec                                               | 2.86 sec: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 334 ms: 1.41x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 325 ms: 1.39x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.38x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 866 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 568 ms: 1.28x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 586 ms: 1.24x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 984 ms: 1.20x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.34x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.6 ms: 1.17x faster                                                |
| float          | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                                 |
| regex_dna      | 212 ms                                                 | 211 ms: 1.00x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 194 us: 1.19x faster                                                 |
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.04x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                         |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                |
| django_template | 34.6 ms                                                | 36.4 ms: 1.05x slower                                                |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 379 ms: 1.51x faster                                                 |
| async_tree_none            | 472 ms                                                 | 334 ms: 1.41x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 325 ms: 1.39x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.38x faster                                                 |
| deepcopy                   | 371 us                                                 | 273 us: 1.36x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.34x faster                                                |
| async_tree_io              | 1.16 sec                                               | 866 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 568 ms: 1.28x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 586 ms: 1.24x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 67.8 ms: 1.21x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 984 ms: 1.20x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.19x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.83 us: 1.18x faster                                                |
| scimark_fft                | 382 ms                                                 | 323 ms: 1.18x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                               |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                |
| nbody                      | 97.0 ms                                                | 82.6 ms: 1.17x faster                                                |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 64.5 ms: 1.16x faster                                                |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                |
| raytrace                   | 312 ms                                                 | 280 ms: 1.12x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                                |
| richards                   | 45.8 ms                                                | 41.2 ms: 1.11x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                |
| float                      | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                |
| go                         | 139 ms                                                 | 128 ms: 1.09x faster                                                 |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.70 ms: 1.08x faster                                                |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                 |
| json                       | 5.26 ms                                                | 4.90 ms: 1.07x faster                                                |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                 |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                 |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                 |
| richards_super             | 51.5 ms                                                | 48.4 ms: 1.06x faster                                                |
| logging_silent             | 104 ns                                                 | 99.5 ns: 1.05x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                               |
| dulwich_log                | 68.5 ms                                                | 65.6 ms: 1.04x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.04x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.04x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.04x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 749 ms: 1.04x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                               |
| async_generators           | 463 ms                                                 | 460 ms: 1.01x faster                                                 |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                 |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.00x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                 |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 55.5 ms: 1.01x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                |
| docutils                   | 2.77 sec                                               | 2.86 sec: 1.03x slower                                               |
| bench_thread_pool          | 842 us                                                 | 876 us: 1.04x slower                                                 |
| sympy_expand               | 478 ms                                                 | 498 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.4 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                 |
| nqueens                    | 83.3 ms                                                | 89.2 ms: 1.07x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                |
| telco                      | 7.10 ms                                                | 7.72 ms: 1.09x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.98 ms: 1.09x slower                                                |
| generators                 | 31.2 ms                                                | 35.8 ms: 1.15x slower                                                |
| coverage                   | 72.7 ms                                                | 86.2 ms: 1.19x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.52 ms: 1.19x slower                                                |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 78.3 ms: 3.26x slower                                                |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (1): pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241111-3.14.0a1+-1723e00-JIT/bm-20241111-linux-x86_64-brandtbucher-warmup_16384-3.14.0a1+-1723e00.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.067x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x