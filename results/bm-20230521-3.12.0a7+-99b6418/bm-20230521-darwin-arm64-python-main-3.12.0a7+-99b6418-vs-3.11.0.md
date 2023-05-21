
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 99b6418
- commit date: 2023-05-21
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 173 ms: 1.07x slower                                   |
| docutils       | 1.47 sec                                               | 1.53 sec: 1.04x slower                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 67.4 ms: 1.03x slower                                  |
| float          | 53.0 ms                                                | 58.6 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 151 ms: 1.01x faster                                   |
| regex_v8       | 16.1 ms                                                | 16.2 ms: 1.01x slower                                  |
| regex_effbot   | 2.63 ms                                                | 2.69 ms: 1.02x slower                                  |
| regex_compile  | 76.7 ms                                                | 78.8 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.94 ms: 1.10x faster                                  |
| unpickle_pure_python | 159 us                                                 | 152 us: 1.04x faster                                   |
| pickle_pure_python   | 201 us                                                 | 195 us: 1.03x faster                                   |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.01x slower                                   |
| tomli_loads          | 1.47 sec                                               | 1.50 sec: 1.02x slower                                 |
| unpickle             | 9.67 us                                                | 9.91 us: 1.02x slower                                  |
| pickle_dict          | 18.0 us                                                | 19.0 us: 1.06x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 76.3 ms: 1.09x slower                                  |
| pickle_list          | 2.81 us                                                | 3.08 us: 1.10x slower                                  |
| json_loads           | 16.1 us                                                | 17.8 us: 1.10x slower                                  |
| pickle               | 7.15 us                                                | 7.92 us: 1.11x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 40.5 ms: 1.15x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 58.3 ms: 1.21x slower                                  |
| unpickle_list        | 2.65 us                                                | 3.28 us: 1.24x slower                                  |
| Geometric mean       | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.9 ms: 1.04x slower                                  |
| python_startup_no_site | 10.2 ms                                                | 10.8 ms: 1.07x slower                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.81 ms: 1.09x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 91.7 us: 3.66x faster                                  |
| asyncio_tcp              | 651 ms                                                 | 456 ms: 1.43x faster                                   |
| unpack_sequence          | 34.1 ns                                                | 28.5 ns: 1.20x faster                                  |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.25 sec: 1.15x faster                                 |
| deltablue                | 2.81 ms                                                | 2.49 ms: 1.13x faster                                  |
| generators               | 28.8 ms                                                | 25.8 ms: 1.11x faster                                  |
| json_dumps               | 7.63 ms                                                | 6.94 ms: 1.10x faster                                  |
| mako                     | 8.53 ms                                                | 7.81 ms: 1.09x faster                                  |
| hexiom                   | 4.72 ms                                                | 4.35 ms: 1.08x faster                                  |
| async_tree_none          | 286 ms                                                 | 268 ms: 1.07x faster                                   |
| async_tree_memoization   | 336 ms                                                 | 315 ms: 1.07x faster                                   |
| richards_super           | 39.2 ms                                                | 36.9 ms: 1.06x faster                                  |
| sqlglot_parse            | 959 us                                                 | 910 us: 1.05x faster                                   |
| unpickle_pure_python     | 159 us                                                 | 152 us: 1.04x faster                                   |
| chaos                    | 49.4 ms                                                | 47.3 ms: 1.04x faster                                  |
| async_tree_io            | 704 ms                                                 | 676 ms: 1.04x faster                                   |
| sqlglot_transpile        | 1.12 ms                                                | 1.09 ms: 1.03x faster                                  |
| pickle_pure_python       | 201 us                                                 | 195 us: 1.03x faster                                   |
| deepcopy_memo            | 26.3 us                                                | 25.6 us: 1.03x faster                                  |
| coverage                 | 58.4 ms                                                | 57.1 ms: 1.02x faster                                  |
| create_gc_cycles         | 716 us                                                 | 701 us: 1.02x faster                                   |
| regex_dna                | 152 ms                                                 | 151 ms: 1.01x faster                                   |
| gc_traversal             | 2.42 ms                                                | 2.42 ms: 1.00x slower                                  |
| regex_v8                 | 16.1 ms                                                | 16.2 ms: 1.01x slower                                  |
| meteor_contest           | 73.5 ms                                                | 74.3 ms: 1.01x slower                                  |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.01x slower                                   |
| richards                 | 32.2 ms                                                | 32.8 ms: 1.02x slower                                  |
| mdp                      | 1.55 sec                                               | 1.57 sec: 1.02x slower                                 |
| go                       | 109 ms                                                 | 110 ms: 1.02x slower                                   |
| scimark_sor              | 82.6 ms                                                | 84.4 ms: 1.02x slower                                  |
| dulwich_log              | 30.3 ms                                                | 31.0 ms: 1.02x slower                                  |
| tomli_loads              | 1.47 sec                                               | 1.50 sec: 1.02x slower                                 |
| unpickle                 | 9.67 us                                                | 9.91 us: 1.02x slower                                  |
| regex_effbot             | 2.63 ms                                                | 2.69 ms: 1.02x slower                                  |
| regex_compile            | 76.7 ms                                                | 78.8 ms: 1.03x slower                                  |
| nbody                    | 65.6 ms                                                | 67.4 ms: 1.03x slower                                  |
| coroutines               | 17.8 ms                                                | 18.3 ms: 1.03x slower                                  |
| pathlib                  | 27.2 ms                                                | 28.1 ms: 1.03x slower                                  |
| comprehensions           | 16.1 us                                                | 16.7 us: 1.04x slower                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.31 ms: 1.04x slower                                  |
| python_startup           | 12.4 ms                                                | 12.9 ms: 1.04x slower                                  |
| docutils                 | 1.47 sec                                               | 1.53 sec: 1.04x slower                                 |
| bench_thread_pool        | 474 us                                                 | 495 us: 1.04x slower                                   |
| scimark_fft              | 200 ms                                                 | 209 ms: 1.05x slower                                   |
| pickle_dict              | 18.0 us                                                | 19.0 us: 1.06x slower                                  |
| logging_simple           | 3.55 us                                                | 3.75 us: 1.06x slower                                  |
| crypto_pyaes             | 51.7 ms                                                | 54.9 ms: 1.06x slower                                  |
| logging_silent           | 68.1 ns                                                | 72.4 ns: 1.06x slower                                  |
| python_startup_no_site   | 10.2 ms                                                | 10.8 ms: 1.07x slower                                  |
| fannkuch                 | 261 ms                                                 | 279 ms: 1.07x slower                                   |
| logging_format           | 3.78 us                                                | 4.04 us: 1.07x slower                                  |
| nqueens                  | 59.8 ms                                                | 64.0 ms: 1.07x slower                                  |
| 2to3                     | 161 ms                                                 | 173 ms: 1.07x slower                                   |
| deepcopy                 | 223 us                                                 | 239 us: 1.08x slower                                   |
| sqlalchemy_declarative   | 62.6 ms                                                | 67.6 ms: 1.08x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.03 sec: 1.08x slower                                 |
| spectral_norm            | 72.6 ms                                                | 78.9 ms: 1.09x slower                                  |
| pprint_safe_repr         | 466 ms                                                 | 507 ms: 1.09x slower                                   |
| xml_etree_iterparse      | 70.1 ms                                                | 76.3 ms: 1.09x slower                                  |
| bench_mp_pool            | 43.9 ms                                                | 47.8 ms: 1.09x slower                                  |
| scimark_lu               | 73.3 ms                                                | 80.3 ms: 1.10x slower                                  |
| pickle_list              | 2.81 us                                                | 3.08 us: 1.10x slower                                  |
| json                     | 2.78 ms                                                | 3.05 ms: 1.10x slower                                  |
| json_loads               | 16.1 us                                                | 17.8 us: 1.10x slower                                  |
| float                    | 53.0 ms                                                | 58.6 ms: 1.11x slower                                  |
| pickle                   | 7.15 us                                                | 7.92 us: 1.11x slower                                  |
| pyflate                  | 310 ms                                                 | 344 ms: 1.11x slower                                   |
| scimark_monte_carlo      | 46.5 ms                                                | 52.3 ms: 1.12x slower                                  |
| sqlglot_normalize        | 171 ms                                                 | 194 ms: 1.13x slower                                   |
| deepcopy_reduce          | 1.91 us                                                | 2.17 us: 1.14x slower                                  |
| xml_etree_process        | 35.1 ms                                                | 40.5 ms: 1.15x slower                                  |
| sqlglot_optimize         | 31.1 ms                                                | 36.0 ms: 1.16x slower                                  |
| telco                    | 3.41 ms                                                | 4.07 ms: 1.20x slower                                  |
| raytrace                 | 207 ms                                                 | 250 ms: 1.21x slower                                   |
| xml_etree_generate       | 48.3 ms                                                | 58.3 ms: 1.21x slower                                  |
| unpickle_list            | 2.65 us                                                | 3.28 us: 1.24x slower                                  |
| sqlite_synth             | 1.27 us                                                | 1.59 us: 1.25x slower                                  |
| async_generators         | 196 ms                                                 | 321 ms: 1.64x slower                                   |
| Geometric mean           | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, sqlalchemy_imperative, pidigits, mypy2, tornado_http, pycparser
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230521-3.12.0a7+-99b6418/bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418.json: dask
