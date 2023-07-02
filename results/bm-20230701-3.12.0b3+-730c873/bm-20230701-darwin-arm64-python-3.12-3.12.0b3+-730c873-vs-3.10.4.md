
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: darwin-arm64
- commit hash: 730c873
- commit date: 2023-07-01
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 169 ms: 1.20x faster                                   |
| docutils       | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| tornado_http   | 91.9 ms                                                | 70.6 ms: 1.30x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 68.7 ms: 1.37x faster                                  |
| float          | 72.3 ms                                                | 56.9 ms: 1.27x faster                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.9 ms: 1.27x faster                                  |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                  |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.58 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-3.12-3.12.0b3+-730c873 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 191 us: 1.49x faster                                   |
| unpickle_pure_python | 203 us                                                 | 146 us: 1.39x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.33 ms: 1.32x faster                                  |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| xml_etree_process    | 45.1 ms                                                | 39.1 ms: 1.15x faster                                  |
| unpickle             | 9.77 us                                                | 9.28 us: 1.05x faster                                  |
| pickle               | 7.36 us                                                | 7.40 us: 1.01x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| pickle_list          | 2.83 us                                                | 2.87 us: 1.01x slower                                  |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.03x slower                                   |
| xml_etree_iterparse  | 72.6 ms                                                | 74.9 ms: 1.03x slower                                  |
| xml_etree_generate   | 54.3 ms                                                | 56.2 ms: 1.04x slower                                  |
| json_loads           | 16.9 us                                                | 17.5 us: 1.04x slower                                  |
| unpickle_list        | 2.66 us                                                | 3.28 us: 1.23x slower                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-3.12-3.12.0b3+-730c873 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.3 ms: 1.12x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 9.15 ms: 1.06x faster                                  |
| Geometric mean         | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-3.12-3.12.0b3+-730c873 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.60 ms: 1.38x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230701-darwin-arm64-python-3.12-3.12.0b3+-730c873 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 90.6 us: 3.80x faster                                  |
| deltablue                | 5.15 ms                                                | 2.43 ms: 2.12x faster                                  |
| richards_super           | 60.7 ms                                                | 34.2 ms: 1.77x faster                                  |
| go                       | 165 ms                                                 | 94.0 ms: 1.75x faster                                  |
| logging_silent           | 119 ns                                                 | 69.1 ns: 1.72x faster                                  |
| richards                 | 51.4 ms                                                | 30.5 ms: 1.69x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 43.3 ms: 1.67x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 829 us: 1.61x faster                                   |
| chaos                    | 66.8 ms                                                | 41.8 ms: 1.60x faster                                  |
| async_tree_memoization   | 493 ms                                                 | 311 ms: 1.58x faster                                   |
| raytrace                 | 328 ms                                                 | 210 ms: 1.56x faster                                   |
| sqlglot_transpile        | 1.54 ms                                                | 1.00 ms: 1.53x faster                                  |
| async_tree_io            | 1.02 sec                                               | 665 ms: 1.53x faster                                   |
| scimark_lu               | 110 ms                                                 | 72.4 ms: 1.52x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 51.5 ms: 1.52x faster                                  |
| async_tree_none          | 402 ms                                                 | 265 ms: 1.51x faster                                   |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.49x faster                                  |
| pickle_pure_python       | 284 us                                                 | 191 us: 1.49x faster                                   |
| scimark_sor              | 127 ms                                                 | 85.6 ms: 1.48x faster                                  |
| pyflate                  | 453 ms                                                 | 309 ms: 1.47x faster                                   |
| asyncio_tcp              | 673 ms                                                 | 460 ms: 1.46x faster                                   |
| unpickle_pure_python     | 203 us                                                 | 146 us: 1.39x faster                                   |
| mako                     | 10.5 ms                                                | 7.60 ms: 1.38x faster                                  |
| deepcopy_memo            | 34.5 us                                                | 25.1 us: 1.37x faster                                  |
| nbody                    | 94.1 ms                                                | 68.7 ms: 1.37x faster                                  |
| pycparser                | 915 ms                                                 | 673 ms: 1.36x faster                                   |
| unpack_sequence          | 38.7 ns                                                | 28.8 ns: 1.34x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.33 ms: 1.32x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.25 sec: 1.32x faster                                 |
| sqlalchemy_imperative    | 9.03 ms                                                | 6.87 ms: 1.31x faster                                  |
| tornado_http             | 91.9 ms                                                | 70.6 ms: 1.30x faster                                  |
| spectral_norm            | 96.4 ms                                                | 74.6 ms: 1.29x faster                                  |
| logging_format           | 5.01 us                                                | 3.89 us: 1.29x faster                                  |
| logging_simple           | 4.63 us                                                | 3.60 us: 1.29x faster                                  |
| regex_compile            | 96.6 ms                                                | 75.9 ms: 1.27x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 527 ms: 1.27x faster                                   |
| float                    | 72.3 ms                                                | 56.9 ms: 1.27x faster                                  |
| generators               | 32.9 ms                                                | 26.5 ms: 1.24x faster                                  |
| create_gc_cycles         | 876 us                                                 | 705 us: 1.24x faster                                   |
| dulwich_log              | 37.1 ms                                                | 29.9 ms: 1.24x faster                                  |
| pprint_safe_repr         | 609 ms                                                 | 493 ms: 1.23x faster                                   |
| pprint_pformat           | 1.24 sec                                               | 1.01 sec: 1.23x faster                                 |
| fannkuch                 | 317 ms                                                 | 261 ms: 1.22x faster                                   |
| deepcopy                 | 278 us                                                 | 229 us: 1.22x faster                                   |
| 2to3                     | 202 ms                                                 | 169 ms: 1.20x faster                                   |
| mypy2                    | 308 ms                                                 | 259 ms: 1.19x faster                                   |
| docutils                 | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| comprehensions           | 17.7 us                                                | 15.1 us: 1.17x faster                                  |
| scimark_fft              | 232 ms                                                 | 201 ms: 1.16x faster                                   |
| deepcopy_reduce          | 2.38 us                                                | 2.07 us: 1.15x faster                                  |
| xml_etree_process        | 45.1 ms                                                | 39.1 ms: 1.15x faster                                  |
| coroutines               | 20.2 ms                                                | 17.6 ms: 1.15x faster                                  |
| sqlalchemy_declarative   | 74.8 ms                                                | 65.2 ms: 1.15x faster                                  |
| nqueens                  | 68.1 ms                                                | 60.2 ms: 1.13x faster                                  |
| bench_thread_pool        | 548 us                                                 | 486 us: 1.13x faster                                   |
| python_startup           | 12.6 ms                                                | 11.3 ms: 1.12x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 34.2 ms: 1.11x faster                                  |
| regex_v8                 | 17.5 ms                                                | 15.8 ms: 1.11x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.15 ms: 1.10x faster                                  |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| python_startup_no_site   | 9.73 ms                                                | 9.15 ms: 1.06x faster                                  |
| meteor_contest           | 78.6 ms                                                | 74.1 ms: 1.06x faster                                  |
| sqlglot_normalize        | 197 ms                                                 | 185 ms: 1.06x faster                                   |
| unpickle                 | 9.77 us                                                | 9.28 us: 1.05x faster                                  |
| json                     | 3.10 ms                                                | 3.02 ms: 1.03x faster                                  |
| mdp                      | 1.67 sec                                               | 1.64 sec: 1.02x faster                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                  |
| pickle                   | 7.36 us                                                | 7.40 us: 1.01x slower                                  |
| telco                    | 3.68 ms                                                | 3.71 ms: 1.01x slower                                  |
| pickle_dict              | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| pickle_list              | 2.83 us                                                | 2.87 us: 1.01x slower                                  |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.03x slower                                   |
| xml_etree_iterparse      | 72.6 ms                                                | 74.9 ms: 1.03x slower                                  |
| xml_etree_generate       | 54.3 ms                                                | 56.2 ms: 1.04x slower                                  |
| json_loads               | 16.9 us                                                | 17.5 us: 1.04x slower                                  |
| regex_effbot             | 2.45 ms                                                | 2.58 ms: 1.06x slower                                  |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.09x slower                                  |
| bench_mp_pool            | 41.0 ms                                                | 45.0 ms: 1.10x slower                                  |
| pathlib                  | 28.8 ms                                                | 32.2 ms: 1.12x slower                                  |
| unpickle_list            | 2.66 us                                                | 3.28 us: 1.23x slower                                  |
| coverage                 | 40.8 ms                                                | 50.7 ms: 1.24x slower                                  |
| dask                     | 258 ms                                                 | 320 ms: 1.24x slower                                   |
| async_generators         | 233 ms                                                 | 308 ms: 1.32x slower                                   |
| Geometric mean           | (ref)                                                  | 1.23x faster                                           |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
