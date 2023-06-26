
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: bef1c87
- commit date: 2023-06-25
- overall geometric mean: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.54 sec: 1.16x faster                                |
| tornado_http   | 91.9 ms                                                | 71.8 ms: 1.28x faster                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 71.5 ms: 1.32x faster                                 |
| float          | 72.3 ms                                                | 57.3 ms: 1.26x faster                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.4 ms: 1.28x faster                                 |
| regex_v8       | 17.5 ms                                                | 15.6 ms: 1.12x faster                                 |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.59 ms: 1.06x slower                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 191 us: 1.49x faster                                  |
| unpickle_pure_python | 203 us                                                 | 148 us: 1.37x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.43 ms: 1.30x faster                                 |
| tomli_loads          | 1.76 sec                                               | 1.42 sec: 1.24x faster                                |
| xml_etree_process    | 45.1 ms                                                | 39.2 ms: 1.15x faster                                 |
| unpickle             | 9.77 us                                                | 9.14 us: 1.07x faster                                 |
| pickle_list          | 2.83 us                                                | 2.86 us: 1.01x slower                                 |
| pickle               | 7.36 us                                                | 7.49 us: 1.02x slower                                 |
| pickle_dict          | 17.8 us                                                | 18.2 us: 1.02x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 75.7 ms: 1.04x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 56.6 ms: 1.04x slower                                 |
| json_loads           | 16.9 us                                                | 17.7 us: 1.05x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.14 us: 1.18x slower                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.0 ms: 1.05x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 9.87 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.60 ms: 1.38x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230625-darwin-arm64-python-main-3.13.0a0-bef1c87 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 90.8 us: 3.79x faster                                 |
| deltablue                | 5.15 ms                                                | 2.50 ms: 2.06x faster                                 |
| richards_super           | 60.7 ms                                                | 35.4 ms: 1.72x faster                                 |
| logging_silent           | 119 ns                                                 | 69.6 ns: 1.71x faster                                 |
| go                       | 165 ms                                                 | 98.5 ms: 1.67x faster                                 |
| richards                 | 51.4 ms                                                | 31.8 ms: 1.62x faster                                 |
| asyncio_tcp              | 673 ms                                                 | 416 ms: 1.62x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 836 us: 1.59x faster                                  |
| chaos                    | 66.8 ms                                                | 42.5 ms: 1.57x faster                                 |
| async_tree_memoization   | 493 ms                                                 | 318 ms: 1.55x faster                                  |
| sqlglot_transpile        | 1.54 ms                                                | 1.01 ms: 1.53x faster                                 |
| async_tree_io            | 1.02 sec                                               | 673 ms: 1.52x faster                                  |
| scimark_lu               | 110 ms                                                 | 72.7 ms: 1.51x faster                                 |
| crypto_pyaes             | 78.0 ms                                                | 51.8 ms: 1.51x faster                                 |
| pickle_pure_python       | 284 us                                                 | 191 us: 1.49x faster                                  |
| async_tree_none          | 402 ms                                                 | 271 ms: 1.48x faster                                  |
| raytrace                 | 328 ms                                                 | 222 ms: 1.48x faster                                  |
| scimark_sor              | 127 ms                                                 | 86.9 ms: 1.46x faster                                 |
| hexiom                   | 6.32 ms                                                | 4.39 ms: 1.44x faster                                 |
| scimark_monte_carlo      | 72.2 ms                                                | 51.4 ms: 1.40x faster                                 |
| mako                     | 10.5 ms                                                | 7.60 ms: 1.38x faster                                 |
| unpickle_pure_python     | 203 us                                                 | 148 us: 1.37x faster                                  |
| pyflate                  | 453 ms                                                 | 330 ms: 1.37x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 28.2 ns: 1.37x faster                                 |
| deepcopy_memo            | 34.5 us                                                | 25.8 us: 1.34x faster                                 |
| pycparser                | 915 ms                                                 | 685 ms: 1.34x faster                                  |
| nbody                    | 94.1 ms                                                | 71.5 ms: 1.32x faster                                 |
| json_dumps               | 8.38 ms                                                | 6.43 ms: 1.30x faster                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.26 sec: 1.30x faster                                |
| spectral_norm            | 96.4 ms                                                | 74.7 ms: 1.29x faster                                 |
| tornado_http             | 91.9 ms                                                | 71.8 ms: 1.28x faster                                 |
| regex_compile            | 96.6 ms                                                | 75.4 ms: 1.28x faster                                 |
| logging_format           | 5.01 us                                                | 3.91 us: 1.28x faster                                 |
| logging_simple           | 4.63 us                                                | 3.64 us: 1.27x faster                                 |
| float                    | 72.3 ms                                                | 57.3 ms: 1.26x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 535 ms: 1.25x faster                                  |
| create_gc_cycles         | 876 us                                                 | 700 us: 1.25x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.42 sec: 1.24x faster                                |
| dulwich_log              | 37.1 ms                                                | 30.0 ms: 1.24x faster                                 |
| generators               | 32.9 ms                                                | 26.9 ms: 1.23x faster                                 |
| pprint_pformat           | 1.24 sec                                               | 1.01 sec: 1.22x faster                                |
| pprint_safe_repr         | 609 ms                                                 | 498 ms: 1.22x faster                                  |
| deepcopy                 | 278 us                                                 | 231 us: 1.20x faster                                  |
| mypy2                    | 308 ms                                                 | 259 ms: 1.19x faster                                  |
| fannkuch                 | 317 ms                                                 | 269 ms: 1.18x faster                                  |
| docutils                 | 1.78 sec                                               | 1.54 sec: 1.16x faster                                |
| xml_etree_process        | 45.1 ms                                                | 39.2 ms: 1.15x faster                                 |
| scimark_fft              | 232 ms                                                 | 202 ms: 1.15x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 2.09 us: 1.14x faster                                 |
| nqueens                  | 68.1 ms                                                | 60.1 ms: 1.13x faster                                 |
| regex_v8                 | 17.5 ms                                                | 15.6 ms: 1.12x faster                                 |
| bench_thread_pool        | 548 us                                                 | 492 us: 1.12x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 34.4 ms: 1.11x faster                                 |
| comprehensions           | 17.7 us                                                | 16.2 us: 1.09x faster                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.19 ms: 1.09x faster                                 |
| coroutines               | 20.2 ms                                                | 18.5 ms: 1.09x faster                                 |
| regex_dna                | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| unpickle                 | 9.77 us                                                | 9.14 us: 1.07x faster                                 |
| meteor_contest           | 78.6 ms                                                | 73.7 ms: 1.07x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 185 ms: 1.06x faster                                  |
| python_startup           | 12.6 ms                                                | 12.0 ms: 1.05x faster                                 |
| json                     | 3.10 ms                                                | 2.97 ms: 1.04x faster                                 |
| mdp                      | 1.67 sec                                               | 1.64 sec: 1.02x faster                                |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                  |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                 |
| pickle_list              | 2.83 us                                                | 2.86 us: 1.01x slower                                 |
| python_startup_no_site   | 9.73 ms                                                | 9.87 ms: 1.01x slower                                 |
| pickle                   | 7.36 us                                                | 7.49 us: 1.02x slower                                 |
| pickle_dict              | 17.8 us                                                | 18.2 us: 1.02x slower                                 |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                  |
| telco                    | 3.68 ms                                                | 3.81 ms: 1.03x slower                                 |
| xml_etree_iterparse      | 72.6 ms                                                | 75.7 ms: 1.04x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 56.6 ms: 1.04x slower                                 |
| json_loads               | 16.9 us                                                | 17.7 us: 1.05x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.59 ms: 1.06x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.09x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 45.5 ms: 1.11x slower                                 |
| pathlib                  | 28.8 ms                                                | 33.1 ms: 1.15x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.14 us: 1.18x slower                                 |
| coverage                 | 40.8 ms                                                | 51.0 ms: 1.25x slower                                 |
| async_generators         | 233 ms                                                 | 313 ms: 1.34x slower                                  |
| Geometric mean           | (ref)                                                  | 1.22x faster                                          |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
