# Results vs. 3.12.0

- fork: brandtbucher
- ref: optimize_off_all
- machine: linux-x86_64
- commit hash: dff2fa8
- commit date: 2024-11-17
- overall geometric mean: 1.015x slower
- HPT reliability: 91.27%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 303 ms: 1.11x slower                                                     |
| docutils       | 2.77 sec                                               | 3.27 sec: 1.18x slower                                                   |
| Geometric mean | (ref)                                                  | 1.14x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                     |
| async_tree_none            | 472 ms                                                 | 343 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 330 ms: 1.36x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 430 ms: 1.34x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 882 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 574 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 592 ms: 1.23x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 987 ms: 1.20x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.32x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 81.7 ms: 1.04x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                     |
| nbody          | 97.0 ms                                                | 102 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                    |
| regex_compile  | 148 ms                                                 | 162 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                   |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 229 us: 1.00x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 62.2 ms: 1.01x slower                                                    |
| pickle_pure_python   | 324 us                                                 | 350 us: 1.08x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                    |
| django_template | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 389 ms: 1.48x faster                                                     |
| async_tree_none            | 472 ms                                                 | 343 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 330 ms: 1.36x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 430 ms: 1.34x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 882 ms: 1.31x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 574 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 592 ms: 1.23x faster                                                     |
| deepcopy                   | 371 us                                                 | 303 us: 1.23x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 987 ms: 1.20x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 34.5 us: 1.18x faster                                                    |
| logging_format             | 7.23 us                                                | 6.34 us: 1.14x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 73.5 ms: 1.11x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 3.01 us: 1.11x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.81 us: 1.11x faster                                                    |
| scimark_fft                | 382 ms                                                 | 347 ms: 1.10x faster                                                     |
| comprehensions             | 21.8 us                                                | 19.8 us: 1.10x faster                                                    |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                                    |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                    |
| json                       | 5.26 ms                                                | 4.95 ms: 1.06x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.88 ms: 1.04x faster                                                    |
| float                      | 84.7 ms                                                | 81.7 ms: 1.04x faster                                                    |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.04x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 86.3 ms: 1.03x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 18.1 ms: 1.03x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.63 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 73.6 ms: 1.02x faster                                                    |
| raytrace                   | 312 ms                                                 | 307 ms: 1.02x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 229 us: 1.00x faster                                                     |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.00x faster                                                     |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                     |
| xml_etree_process          | 61.7 ms                                                | 62.2 ms: 1.01x slower                                                    |
| chaos                      | 67.0 ms                                                | 67.6 ms: 1.01x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                    |
| fannkuch                   | 417 ms                                                 | 430 ms: 1.03x slower                                                     |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                     |
| django_template            | 34.6 ms                                                | 35.8 ms: 1.04x slower                                                    |
| dulwich_log                | 68.5 ms                                                | 71.1 ms: 1.04x slower                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 153 ms: 1.04x slower                                                     |
| pyflate                    | 482 ms                                                 | 507 ms: 1.05x slower                                                     |
| nbody                      | 97.0 ms                                                | 102 ms: 1.05x slower                                                     |
| scimark_sor                | 129 ms                                                 | 138 ms: 1.07x slower                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.46 ms: 1.07x slower                                                    |
| pickle_pure_python         | 324 us                                                 | 350 us: 1.08x slower                                                     |
| scimark_lu                 | 118 ms                                                 | 128 ms: 1.08x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                    |
| sympy_str                  | 300 ms                                                 | 325 ms: 1.08x slower                                                     |
| pycparser                  | 1.18 sec                                               | 1.28 sec: 1.09x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 916 us: 1.09x slower                                                     |
| go                         | 139 ms                                                 | 152 ms: 1.09x slower                                                     |
| regex_compile              | 148 ms                                                 | 162 ms: 1.09x slower                                                     |
| richards                   | 45.8 ms                                                | 50.2 ms: 1.10x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                    |
| telco                      | 7.10 ms                                                | 7.83 ms: 1.10x slower                                                    |
| 2to3                       | 274 ms                                                 | 303 ms: 1.11x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 187 ms: 1.11x slower                                                     |
| logging_silent             | 104 ns                                                 | 116 ns: 1.11x slower                                                     |
| spectral_norm              | 115 ms                                                 | 128 ms: 1.12x slower                                                     |
| sympy_expand               | 478 ms                                                 | 535 ms: 1.12x slower                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.88 ms: 1.12x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 179 us: 1.13x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 126 ms: 1.14x slower                                                     |
| richards_super             | 51.5 ms                                                | 58.7 ms: 1.14x slower                                                    |
| nqueens                    | 83.3 ms                                                | 95.0 ms: 1.14x slower                                                    |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                    |
| sympy_integrate            | 21.4 ms                                                | 25.3 ms: 1.18x slower                                                    |
| docutils                   | 2.77 sec                                               | 3.27 sec: 1.18x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.53 ms: 1.19x slower                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 66.6 ms: 1.21x slower                                                    |
| pprint_safe_repr           | 776 ms                                                 | 995 ms: 1.28x slower                                                     |
| generators                 | 31.2 ms                                                | 40.9 ms: 1.31x slower                                                    |
| hexiom                     | 6.41 ms                                                | 8.50 ms: 1.33x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                    |
| pprint_pformat             | 1.57 sec                                               | 2.14 sec: 1.36x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.68 ms: 1.82x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 85.8 ms: 3.58x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (4): async_generators, sqlite_synth, mdp, regex_effbot
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241117-3.14.0a1+-dff2fa8-JIT/bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.015x slower
# HPT report

- Reliability score: 91.27% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.17x