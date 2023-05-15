
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 7d2deaf
- commit date: 2023-05-13
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 174 ms: 1.08x slower                                   |
| docutils       | 1.47 sec                                               | 1.58 sec: 1.07x slower                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 68.5 ms: 1.04x slower                                  |
| float          | 53.0 ms                                                | 58.8 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| regex_v8       | 16.1 ms                                                | 16.3 ms: 1.01x slower                                  |
| regex_compile  | 76.7 ms                                                | 78.6 ms: 1.02x slower                                  |
| regex_effbot   | 2.63 ms                                                | 2.78 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.89 ms: 1.11x faster                                  |
| unpickle_pure_python | 159 us                                                 | 151 us: 1.05x faster                                   |
| pickle_pure_python   | 201 us                                                 | 194 us: 1.03x faster                                   |
| unpickle             | 9.67 us                                                | 9.91 us: 1.02x slower                                  |
| tomli_loads          | 1.47 sec                                               | 1.50 sec: 1.03x slower                                 |
| pickle_dict          | 18.0 us                                                | 19.1 us: 1.06x slower                                  |
| xml_etree_iterparse  | 70.1 ms                                                | 75.2 ms: 1.07x slower                                  |
| pickle               | 7.15 us                                                | 7.81 us: 1.09x slower                                  |
| json_loads           | 16.1 us                                                | 17.7 us: 1.10x slower                                  |
| pickle_list          | 2.81 us                                                | 3.11 us: 1.11x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 40.4 ms: 1.15x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 58.1 ms: 1.20x slower                                  |
| unpickle_list        | 2.65 us                                                | 3.20 us: 1.21x slower                                  |
| Geometric mean       | (ref)                                                  | 1.06x slower                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 12.8 ms: 1.03x slower                                  |
| python_startup_no_site | 10.2 ms                                                | 10.7 ms: 1.06x slower                                  |
| Geometric mean         | (ref)                                                  | 1.04x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 8.53 ms                                                | 7.80 ms: 1.09x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 96.9 us: 3.47x faster                                  |
| asyncio_tcp              | 651 ms                                                 | 465 ms: 1.40x faster                                   |
| unpack_sequence          | 34.1 ns                                                | 28.4 ns: 1.20x faster                                  |
| generators               | 28.8 ms                                                | 24.9 ms: 1.15x faster                                  |
| deltablue                | 2.81 ms                                                | 2.47 ms: 1.14x faster                                  |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.29 sec: 1.12x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.89 ms: 1.11x faster                                  |
| richards_super           | 39.2 ms                                                | 35.6 ms: 1.10x faster                                  |
| hexiom                   | 4.72 ms                                                | 4.30 ms: 1.10x faster                                  |
| mako                     | 8.53 ms                                                | 7.80 ms: 1.09x faster                                  |
| async_tree_none          | 286 ms                                                 | 265 ms: 1.08x faster                                   |
| async_tree_memoization   | 336 ms                                                 | 313 ms: 1.07x faster                                   |
| sqlglot_parse            | 959 us                                                 | 902 us: 1.06x faster                                   |
| unpickle_pure_python     | 159 us                                                 | 151 us: 1.05x faster                                   |
| chaos                    | 49.4 ms                                                | 47.3 ms: 1.05x faster                                  |
| async_tree_io            | 704 ms                                                 | 674 ms: 1.04x faster                                   |
| sqlglot_transpile        | 1.12 ms                                                | 1.08 ms: 1.04x faster                                  |
| deepcopy_memo            | 26.3 us                                                | 25.4 us: 1.04x faster                                  |
| pickle_pure_python       | 201 us                                                 | 194 us: 1.03x faster                                   |
| create_gc_cycles         | 716 us                                                 | 696 us: 1.03x faster                                   |
| coverage                 | 58.4 ms                                                | 57.1 ms: 1.02x faster                                  |
| regex_dna                | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| sqlalchemy_imperative    | 7.20 ms                                                | 7.12 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 528 ms: 1.01x faster                                   |
| meteor_contest           | 73.5 ms                                                | 72.8 ms: 1.01x faster                                  |
| mypy2                    | 195 ms                                                 | 194 ms: 1.00x faster                                   |
| gc_traversal             | 2.42 ms                                                | 2.42 ms: 1.00x slower                                  |
| go                       | 109 ms                                                 | 110 ms: 1.01x slower                                   |
| regex_v8                 | 16.1 ms                                                | 16.3 ms: 1.01x slower                                  |
| mdp                      | 1.55 sec                                               | 1.57 sec: 1.01x slower                                 |
| logging_silent           | 68.1 ns                                                | 69.1 ns: 1.01x slower                                  |
| dulwich_log              | 30.3 ms                                                | 30.8 ms: 1.02x slower                                  |
| comprehensions           | 16.1 us                                                | 16.4 us: 1.02x slower                                  |
| coroutines               | 17.8 ms                                                | 18.2 ms: 1.02x slower                                  |
| regex_compile            | 76.7 ms                                                | 78.6 ms: 1.02x slower                                  |
| unpickle                 | 9.67 us                                                | 9.91 us: 1.02x slower                                  |
| tomli_loads              | 1.47 sec                                               | 1.50 sec: 1.03x slower                                 |
| python_startup           | 12.4 ms                                                | 12.8 ms: 1.03x slower                                  |
| pathlib                  | 27.2 ms                                                | 28.0 ms: 1.03x slower                                  |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.29 ms: 1.03x slower                                  |
| scimark_sor              | 82.6 ms                                                | 85.7 ms: 1.04x slower                                  |
| bench_thread_pool        | 474 us                                                 | 492 us: 1.04x slower                                   |
| scimark_fft              | 200 ms                                                 | 208 ms: 1.04x slower                                   |
| nbody                    | 65.6 ms                                                | 68.5 ms: 1.04x slower                                  |
| logging_simple           | 3.55 us                                                | 3.74 us: 1.05x slower                                  |
| deepcopy                 | 223 us                                                 | 235 us: 1.05x slower                                   |
| regex_effbot             | 2.63 ms                                                | 2.78 ms: 1.06x slower                                  |
| python_startup_no_site   | 10.2 ms                                                | 10.7 ms: 1.06x slower                                  |
| crypto_pyaes             | 51.7 ms                                                | 54.8 ms: 1.06x slower                                  |
| pickle_dict              | 18.0 us                                                | 19.1 us: 1.06x slower                                  |
| fannkuch                 | 261 ms                                                 | 277 ms: 1.06x slower                                   |
| nqueens                  | 59.8 ms                                                | 63.8 ms: 1.07x slower                                  |
| logging_format           | 3.78 us                                                | 4.04 us: 1.07x slower                                  |
| xml_etree_iterparse      | 70.1 ms                                                | 75.2 ms: 1.07x slower                                  |
| docutils                 | 1.47 sec                                               | 1.58 sec: 1.07x slower                                 |
| sqlalchemy_declarative   | 62.6 ms                                                | 67.2 ms: 1.07x slower                                  |
| pprint_pformat           | 954 ms                                                 | 1.03 sec: 1.08x slower                                 |
| 2to3                     | 161 ms                                                 | 174 ms: 1.08x slower                                   |
| pprint_safe_repr         | 466 ms                                                 | 504 ms: 1.08x slower                                   |
| json                     | 2.78 ms                                                | 3.02 ms: 1.09x slower                                  |
| spectral_norm            | 72.6 ms                                                | 79.0 ms: 1.09x slower                                  |
| scimark_lu               | 73.3 ms                                                | 79.9 ms: 1.09x slower                                  |
| bench_mp_pool            | 43.9 ms                                                | 48.0 ms: 1.09x slower                                  |
| pickle                   | 7.15 us                                                | 7.81 us: 1.09x slower                                  |
| json_loads               | 16.1 us                                                | 17.7 us: 1.10x slower                                  |
| pyflate                  | 310 ms                                                 | 342 ms: 1.10x slower                                   |
| pickle_list              | 2.81 us                                                | 3.11 us: 1.11x slower                                  |
| float                    | 53.0 ms                                                | 58.8 ms: 1.11x slower                                  |
| sqlglot_normalize        | 171 ms                                                 | 190 ms: 1.11x slower                                   |
| scimark_monte_carlo      | 46.5 ms                                                | 52.1 ms: 1.12x slower                                  |
| deepcopy_reduce          | 1.91 us                                                | 2.14 us: 1.12x slower                                  |
| sqlglot_optimize         | 31.1 ms                                                | 35.5 ms: 1.14x slower                                  |
| xml_etree_process        | 35.1 ms                                                | 40.4 ms: 1.15x slower                                  |
| telco                    | 3.41 ms                                                | 3.94 ms: 1.16x slower                                  |
| xml_etree_generate       | 48.3 ms                                                | 58.1 ms: 1.20x slower                                  |
| raytrace                 | 207 ms                                                 | 249 ms: 1.21x slower                                   |
| unpickle_list            | 2.65 us                                                | 3.20 us: 1.21x slower                                  |
| sqlite_synth             | 1.27 us                                                | 1.58 us: 1.24x slower                                  |
| async_generators         | 196 ms                                                 | 319 ms: 1.63x slower                                   |
| Geometric mean           | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (5): tornado_http, pidigits, richards, pycparser, xml_etree_parse
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230513-3.12.0a7+-7d2deaf/bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf.json: dask
