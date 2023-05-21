
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 99b6418
- commit date: 2023-05-21
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 173 ms: 1.17x faster                                   |
| docutils       | 1.78 sec                                               | 1.53 sec: 1.17x faster                                 |
| tornado_http   | 91.9 ms                                                | 71.6 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 67.4 ms: 1.40x faster                                  |
| float          | 72.3 ms                                                | 58.6 ms: 1.23x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 78.8 ms: 1.23x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.2 ms: 1.08x faster                                  |
| regex_dna      | 160 ms                                                 | 151 ms: 1.06x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.69 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 195 us: 1.45x faster                                   |
| unpickle_pure_python | 203 us                                                 | 152 us: 1.33x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.94 ms: 1.21x faster                                  |
| tomli_loads          | 1.76 sec                                               | 1.50 sec: 1.17x faster                                 |
| xml_etree_process    | 45.1 ms                                                | 40.5 ms: 1.11x faster                                  |
| unpickle             | 9.77 us                                                | 9.91 us: 1.01x slower                                  |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                   |
| xml_etree_iterparse  | 72.6 ms                                                | 76.3 ms: 1.05x slower                                  |
| json_loads           | 16.9 us                                                | 17.8 us: 1.05x slower                                  |
| pickle_dict          | 17.8 us                                                | 19.0 us: 1.07x slower                                  |
| xml_etree_generate   | 54.3 ms                                                | 58.3 ms: 1.08x slower                                  |
| pickle               | 7.36 us                                                | 7.92 us: 1.08x slower                                  |
| pickle_list          | 2.83 us                                                | 3.08 us: 1.09x slower                                  |
| unpickle_list        | 2.66 us                                                | 3.28 us: 1.23x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.9 ms: 1.02x slower                                  |
| python_startup_no_site | 9.73 ms                                                | 10.8 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.81 ms: 1.34x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230521-darwin-arm64-python-main-3.12.0a7+-99b6418 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 91.7 us: 3.75x faster                                  |
| deltablue                | 5.15 ms                                                | 2.49 ms: 2.07x faster                                  |
| logging_silent           | 119 ns                                                 | 72.4 ns: 1.65x faster                                  |
| richards_super           | 60.7 ms                                                | 36.9 ms: 1.64x faster                                  |
| mypy2                    | 308 ms                                                 | 195 ms: 1.58x faster                                   |
| richards                 | 51.4 ms                                                | 32.8 ms: 1.57x faster                                  |
| async_tree_memoization   | 493 ms                                                 | 315 ms: 1.57x faster                                   |
| async_tree_io            | 1.02 sec                                               | 676 ms: 1.51x faster                                   |
| async_tree_none          | 402 ms                                                 | 268 ms: 1.50x faster                                   |
| scimark_sor              | 127 ms                                                 | 84.4 ms: 1.50x faster                                  |
| go                       | 165 ms                                                 | 110 ms: 1.49x faster                                   |
| asyncio_tcp              | 673 ms                                                 | 456 ms: 1.48x faster                                   |
| sqlglot_parse            | 1.33 ms                                                | 910 us: 1.46x faster                                   |
| pickle_pure_python       | 284 us                                                 | 195 us: 1.45x faster                                   |
| hexiom                   | 6.32 ms                                                | 4.35 ms: 1.45x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 54.9 ms: 1.42x faster                                  |
| chaos                    | 66.8 ms                                                | 47.3 ms: 1.41x faster                                  |
| sqlglot_transpile        | 1.54 ms                                                | 1.09 ms: 1.41x faster                                  |
| nbody                    | 94.1 ms                                                | 67.4 ms: 1.40x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 52.3 ms: 1.38x faster                                  |
| scimark_lu               | 110 ms                                                 | 80.3 ms: 1.37x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 28.5 ns: 1.35x faster                                  |
| deepcopy_memo            | 34.5 us                                                | 25.6 us: 1.35x faster                                  |
| mako                     | 10.5 ms                                                | 7.81 ms: 1.34x faster                                  |
| unpickle_pure_python     | 203 us                                                 | 152 us: 1.33x faster                                   |
| pyflate                  | 453 ms                                                 | 344 ms: 1.32x faster                                   |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.25 sec: 1.32x faster                                 |
| raytrace                 | 328 ms                                                 | 250 ms: 1.31x faster                                   |
| pycparser                | 915 ms                                                 | 702 ms: 1.30x faster                                   |
| tornado_http             | 91.9 ms                                                | 71.6 ms: 1.28x faster                                  |
| generators               | 32.9 ms                                                | 25.8 ms: 1.28x faster                                  |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 533 ms: 1.26x faster                                   |
| sqlalchemy_imperative    | 9.03 ms                                                | 7.19 ms: 1.26x faster                                  |
| create_gc_cycles         | 876 us                                                 | 701 us: 1.25x faster                                   |
| logging_format           | 5.01 us                                                | 4.04 us: 1.24x faster                                  |
| logging_simple           | 4.63 us                                                | 3.75 us: 1.23x faster                                  |
| float                    | 72.3 ms                                                | 58.6 ms: 1.23x faster                                  |
| regex_compile            | 96.6 ms                                                | 78.8 ms: 1.23x faster                                  |
| spectral_norm            | 96.4 ms                                                | 78.9 ms: 1.22x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.94 ms: 1.21x faster                                  |
| pprint_pformat           | 1.24 sec                                               | 1.03 sec: 1.20x faster                                 |
| pprint_safe_repr         | 609 ms                                                 | 507 ms: 1.20x faster                                   |
| dulwich_log              | 37.1 ms                                                | 31.0 ms: 1.20x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.50 sec: 1.17x faster                                 |
| 2to3                     | 202 ms                                                 | 173 ms: 1.17x faster                                   |
| docutils                 | 1.78 sec                                               | 1.53 sec: 1.17x faster                                 |
| deepcopy                 | 278 us                                                 | 239 us: 1.16x faster                                   |
| fannkuch                 | 317 ms                                                 | 279 ms: 1.14x faster                                   |
| xml_etree_process        | 45.1 ms                                                | 40.5 ms: 1.11x faster                                  |
| scimark_fft              | 232 ms                                                 | 209 ms: 1.11x faster                                   |
| bench_thread_pool        | 548 us                                                 | 495 us: 1.11x faster                                   |
| sqlalchemy_declarative   | 74.8 ms                                                | 67.6 ms: 1.11x faster                                  |
| coroutines               | 20.2 ms                                                | 18.3 ms: 1.10x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 2.17 us: 1.10x faster                                  |
| regex_v8                 | 17.5 ms                                                | 16.2 ms: 1.08x faster                                  |
| nqueens                  | 68.1 ms                                                | 64.0 ms: 1.06x faster                                  |
| mdp                      | 1.67 sec                                               | 1.57 sec: 1.06x faster                                 |
| regex_dna                | 160 ms                                                 | 151 ms: 1.06x faster                                   |
| comprehensions           | 17.7 us                                                | 16.7 us: 1.06x faster                                  |
| meteor_contest           | 78.6 ms                                                | 74.3 ms: 1.06x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 36.0 ms: 1.05x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.31 ms: 1.05x faster                                  |
| pathlib                  | 28.8 ms                                                | 28.1 ms: 1.03x faster                                  |
| json                     | 3.10 ms                                                | 3.05 ms: 1.01x faster                                  |
| sqlglot_normalize        | 197 ms                                                 | 194 ms: 1.01x faster                                   |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| gc_traversal             | 2.40 ms                                                | 2.42 ms: 1.01x slower                                  |
| unpickle                 | 9.77 us                                                | 9.91 us: 1.01x slower                                  |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.02x slower                                   |
| python_startup           | 12.6 ms                                                | 12.9 ms: 1.02x slower                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 76.3 ms: 1.05x slower                                  |
| json_loads               | 16.9 us                                                | 17.8 us: 1.05x slower                                  |
| pickle_dict              | 17.8 us                                                | 19.0 us: 1.07x slower                                  |
| xml_etree_generate       | 54.3 ms                                                | 58.3 ms: 1.08x slower                                  |
| pickle                   | 7.36 us                                                | 7.92 us: 1.08x slower                                  |
| sqlite_synth             | 1.47 us                                                | 1.59 us: 1.08x slower                                  |
| pickle_list              | 2.83 us                                                | 3.08 us: 1.09x slower                                  |
| regex_effbot             | 2.45 ms                                                | 2.69 ms: 1.10x slower                                  |
| telco                    | 3.68 ms                                                | 4.07 ms: 1.11x slower                                  |
| python_startup_no_site   | 9.73 ms                                                | 10.8 ms: 1.11x slower                                  |
| bench_mp_pool            | 41.0 ms                                                | 47.8 ms: 1.17x slower                                  |
| unpickle_list            | 2.66 us                                                | 3.28 us: 1.23x slower                                  |
| dask                     | 258 ms                                                 | 333 ms: 1.29x slower                                   |
| async_generators         | 233 ms                                                 | 321 ms: 1.38x slower                                   |
| coverage                 | 40.8 ms                                                | 57.1 ms: 1.40x slower                                  |
| Geometric mean           | (ref)                                                  | 1.19x faster                                           |
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
