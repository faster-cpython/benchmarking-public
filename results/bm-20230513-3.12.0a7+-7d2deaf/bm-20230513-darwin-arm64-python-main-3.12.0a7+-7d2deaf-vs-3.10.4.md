
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 7d2deaf
- commit date: 2023-05-13
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 174 ms: 1.17x faster                                   |
| docutils       | 1.78 sec                                               | 1.58 sec: 1.13x faster                                 |
| tornado_http   | 91.9 ms                                                | 70.2 ms: 1.31x faster                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 68.5 ms: 1.37x faster                                  |
| float          | 72.3 ms                                                | 58.8 ms: 1.23x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 78.6 ms: 1.23x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.3 ms: 1.07x faster                                  |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.78 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 194 us: 1.46x faster                                   |
| unpickle_pure_python | 203 us                                                 | 151 us: 1.34x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.89 ms: 1.22x faster                                  |
| tomli_loads          | 1.76 sec                                               | 1.50 sec: 1.17x faster                                 |
| xml_etree_process    | 45.1 ms                                                | 40.4 ms: 1.12x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 108 ms: 1.01x slower                                   |
| unpickle             | 9.77 us                                                | 9.91 us: 1.01x slower                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 75.2 ms: 1.04x slower                                  |
| json_loads           | 16.9 us                                                | 17.7 us: 1.05x slower                                  |
| pickle               | 7.36 us                                                | 7.81 us: 1.06x slower                                  |
| xml_etree_generate   | 54.3 ms                                                | 58.1 ms: 1.07x slower                                  |
| pickle_dict          | 17.8 us                                                | 19.1 us: 1.07x slower                                  |
| pickle_list          | 2.83 us                                                | 3.11 us: 1.10x slower                                  |
| unpickle_list        | 2.66 us                                                | 3.20 us: 1.20x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.8 ms: 1.01x slower                                  |
| python_startup_no_site | 9.73 ms                                                | 10.7 ms: 1.10x slower                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.80 ms: 1.34x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230513-darwin-arm64-python-main-3.12.0a7+-7d2deaf |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 96.9 us: 3.55x faster                                  |
| deltablue                | 5.15 ms                                                | 2.47 ms: 2.08x faster                                  |
| logging_silent           | 119 ns                                                 | 69.1 ns: 1.72x faster                                  |
| richards_super           | 60.7 ms                                                | 35.6 ms: 1.70x faster                                  |
| richards                 | 51.4 ms                                                | 32.3 ms: 1.59x faster                                  |
| mypy2                    | 308 ms                                                 | 194 ms: 1.59x faster                                   |
| async_tree_memoization   | 493 ms                                                 | 313 ms: 1.57x faster                                   |
| async_tree_none          | 402 ms                                                 | 265 ms: 1.52x faster                                   |
| async_tree_io            | 1.02 sec                                               | 674 ms: 1.51x faster                                   |
| go                       | 165 ms                                                 | 110 ms: 1.50x faster                                   |
| scimark_sor              | 127 ms                                                 | 85.7 ms: 1.48x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 902 us: 1.48x faster                                   |
| hexiom                   | 6.32 ms                                                | 4.30 ms: 1.47x faster                                  |
| pickle_pure_python       | 284 us                                                 | 194 us: 1.46x faster                                   |
| asyncio_tcp              | 673 ms                                                 | 465 ms: 1.45x faster                                   |
| sqlglot_transpile        | 1.54 ms                                                | 1.08 ms: 1.42x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 54.8 ms: 1.42x faster                                  |
| chaos                    | 66.8 ms                                                | 47.3 ms: 1.41x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 52.1 ms: 1.39x faster                                  |
| scimark_lu               | 110 ms                                                 | 79.9 ms: 1.38x faster                                  |
| nbody                    | 94.1 ms                                                | 68.5 ms: 1.37x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 28.4 ns: 1.36x faster                                  |
| deepcopy_memo            | 34.5 us                                                | 25.4 us: 1.36x faster                                  |
| unpickle_pure_python     | 203 us                                                 | 151 us: 1.34x faster                                   |
| mako                     | 10.5 ms                                                | 7.80 ms: 1.34x faster                                  |
| pyflate                  | 453 ms                                                 | 342 ms: 1.33x faster                                   |
| generators               | 32.9 ms                                                | 24.9 ms: 1.32x faster                                  |
| raytrace                 | 328 ms                                                 | 249 ms: 1.31x faster                                   |
| pycparser                | 915 ms                                                 | 698 ms: 1.31x faster                                   |
| tornado_http             | 91.9 ms                                                | 70.2 ms: 1.31x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.29 sec: 1.27x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 528 ms: 1.27x faster                                   |
| sqlalchemy_imperative    | 9.03 ms                                                | 7.12 ms: 1.27x faster                                  |
| create_gc_cycles         | 876 us                                                 | 696 us: 1.26x faster                                   |
| logging_format           | 5.01 us                                                | 4.04 us: 1.24x faster                                  |
| logging_simple           | 4.63 us                                                | 3.74 us: 1.24x faster                                  |
| float                    | 72.3 ms                                                | 58.8 ms: 1.23x faster                                  |
| regex_compile            | 96.6 ms                                                | 78.6 ms: 1.23x faster                                  |
| spectral_norm            | 96.4 ms                                                | 79.0 ms: 1.22x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.89 ms: 1.22x faster                                  |
| pprint_pformat           | 1.24 sec                                               | 1.03 sec: 1.21x faster                                 |
| pprint_safe_repr         | 609 ms                                                 | 504 ms: 1.21x faster                                   |
| dulwich_log              | 37.1 ms                                                | 30.8 ms: 1.20x faster                                  |
| deepcopy                 | 278 us                                                 | 235 us: 1.18x faster                                   |
| tomli_loads              | 1.76 sec                                               | 1.50 sec: 1.17x faster                                 |
| 2to3                     | 202 ms                                                 | 174 ms: 1.17x faster                                   |
| fannkuch                 | 317 ms                                                 | 277 ms: 1.14x faster                                   |
| docutils                 | 1.78 sec                                               | 1.58 sec: 1.13x faster                                 |
| xml_etree_process        | 45.1 ms                                                | 40.4 ms: 1.12x faster                                  |
| scimark_fft              | 232 ms                                                 | 208 ms: 1.11x faster                                   |
| sqlalchemy_declarative   | 74.8 ms                                                | 67.2 ms: 1.11x faster                                  |
| bench_thread_pool        | 548 us                                                 | 492 us: 1.11x faster                                   |
| deepcopy_reduce          | 2.38 us                                                | 2.14 us: 1.11x faster                                  |
| coroutines               | 20.2 ms                                                | 18.2 ms: 1.11x faster                                  |
| meteor_contest           | 78.6 ms                                                | 72.8 ms: 1.08x faster                                  |
| comprehensions           | 17.7 us                                                | 16.4 us: 1.07x faster                                  |
| regex_v8                 | 17.5 ms                                                | 16.3 ms: 1.07x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 35.5 ms: 1.07x faster                                  |
| regex_dna                | 160 ms                                                 | 149 ms: 1.07x faster                                   |
| nqueens                  | 68.1 ms                                                | 63.8 ms: 1.07x faster                                  |
| mdp                      | 1.67 sec                                               | 1.57 sec: 1.07x faster                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.29 ms: 1.06x faster                                  |
| sqlglot_normalize        | 197 ms                                                 | 190 ms: 1.03x faster                                   |
| pathlib                  | 28.8 ms                                                | 28.0 ms: 1.03x faster                                  |
| json                     | 3.10 ms                                                | 3.02 ms: 1.03x faster                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| xml_etree_parse          | 107 ms                                                 | 108 ms: 1.01x slower                                   |
| gc_traversal             | 2.40 ms                                                | 2.42 ms: 1.01x slower                                  |
| python_startup           | 12.6 ms                                                | 12.8 ms: 1.01x slower                                  |
| unpickle                 | 9.77 us                                                | 9.91 us: 1.01x slower                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 75.2 ms: 1.04x slower                                  |
| json_loads               | 16.9 us                                                | 17.7 us: 1.05x slower                                  |
| pickle                   | 7.36 us                                                | 7.81 us: 1.06x slower                                  |
| xml_etree_generate       | 54.3 ms                                                | 58.1 ms: 1.07x slower                                  |
| pickle_dict              | 17.8 us                                                | 19.1 us: 1.07x slower                                  |
| telco                    | 3.68 ms                                                | 3.94 ms: 1.07x slower                                  |
| sqlite_synth             | 1.47 us                                                | 1.58 us: 1.07x slower                                  |
| pickle_list              | 2.83 us                                                | 3.11 us: 1.10x slower                                  |
| python_startup_no_site   | 9.73 ms                                                | 10.7 ms: 1.10x slower                                  |
| regex_effbot             | 2.45 ms                                                | 2.78 ms: 1.14x slower                                  |
| bench_mp_pool            | 41.0 ms                                                | 48.0 ms: 1.17x slower                                  |
| unpickle_list            | 2.66 us                                                | 3.20 us: 1.20x slower                                  |
| dask                     | 258 ms                                                 | 333 ms: 1.29x slower                                   |
| async_generators         | 233 ms                                                 | 319 ms: 1.37x slower                                   |
| coverage                 | 40.8 ms                                                | 57.1 ms: 1.40x slower                                  |
| Geometric mean           | (ref)                                                  | 1.19x faster                                           |
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
