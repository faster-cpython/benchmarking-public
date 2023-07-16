
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: darwin-arm64
- commit hash: 30c127f
- commit date: 2023-07-15
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-darwin-arm64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 169 ms: 1.20x faster                                   |
| docutils       | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| tornado_http   | 91.9 ms                                                | 69.2 ms: 1.33x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-darwin-arm64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 68.9 ms: 1.37x faster                                  |
| float          | 72.3 ms                                                | 57.1 ms: 1.27x faster                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-darwin-arm64-python-3.12-3.12.0b4+-30c127f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 76.0 ms: 1.27x faster                                  |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                  |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.61 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-darwin-arm64-python-3.12-3.12.0b4+-30c127f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 191 us: 1.48x faster                                   |
| unpickle_pure_python | 203 us                                                 | 147 us: 1.39x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.30 ms: 1.33x faster                                  |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| xml_etree_process    | 45.1 ms                                                | 38.8 ms: 1.16x faster                                  |
| unpickle             | 9.77 us                                                | 9.30 us: 1.05x faster                                  |
| pickle               | 7.36 us                                                | 7.40 us: 1.01x slower                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                   |
| xml_etree_generate   | 54.3 ms                                                | 56.0 ms: 1.03x slower                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 75.0 ms: 1.03x slower                                  |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                  |
| unpickle_list        | 2.66 us                                                | 3.19 us: 1.20x slower                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-darwin-arm64-python-3.12-3.12.0b4+-30c127f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.1 ms: 1.04x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 9.96 ms: 1.02x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-darwin-arm64-python-3.12-3.12.0b4+-30c127f |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.59 ms: 1.38x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230715-darwin-arm64-python-3.12-3.12.0b4+-30c127f |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 91.4 us: 3.76x faster                                  |
| deltablue                | 5.15 ms                                                | 2.42 ms: 2.13x faster                                  |
| richards_super           | 60.7 ms                                                | 34.1 ms: 1.78x faster                                  |
| go                       | 165 ms                                                 | 94.5 ms: 1.74x faster                                  |
| logging_silent           | 119 ns                                                 | 68.9 ns: 1.73x faster                                  |
| richards                 | 51.4 ms                                                | 30.3 ms: 1.69x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 43.3 ms: 1.67x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 827 us: 1.61x faster                                   |
| chaos                    | 66.8 ms                                                | 42.1 ms: 1.59x faster                                  |
| async_tree_memoization   | 493 ms                                                 | 311 ms: 1.58x faster                                   |
| raytrace                 | 328 ms                                                 | 208 ms: 1.58x faster                                   |
| sqlglot_transpile        | 1.54 ms                                                | 999 us: 1.54x faster                                   |
| async_tree_io            | 1.02 sec                                               | 664 ms: 1.54x faster                                   |
| async_tree_none          | 402 ms                                                 | 265 ms: 1.52x faster                                   |
| crypto_pyaes             | 78.0 ms                                                | 51.5 ms: 1.52x faster                                  |
| scimark_lu               | 110 ms                                                 | 72.7 ms: 1.51x faster                                  |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.49x faster                                  |
| pickle_pure_python       | 284 us                                                 | 191 us: 1.48x faster                                   |
| scimark_sor              | 127 ms                                                 | 85.9 ms: 1.47x faster                                  |
| pyflate                  | 453 ms                                                 | 309 ms: 1.47x faster                                   |
| asyncio_tcp              | 673 ms                                                 | 481 ms: 1.40x faster                                   |
| unpickle_pure_python     | 203 us                                                 | 147 us: 1.39x faster                                   |
| deepcopy_memo            | 34.5 us                                                | 24.9 us: 1.38x faster                                  |
| mako                     | 10.5 ms                                                | 7.59 ms: 1.38x faster                                  |
| nbody                    | 94.1 ms                                                | 68.9 ms: 1.37x faster                                  |
| pycparser                | 915 ms                                                 | 671 ms: 1.36x faster                                   |
| unpack_sequence          | 38.7 ns                                                | 28.7 ns: 1.35x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.30 ms: 1.33x faster                                  |
| tornado_http             | 91.9 ms                                                | 69.2 ms: 1.33x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.27 sec: 1.30x faster                                 |
| logging_format           | 5.01 us                                                | 3.86 us: 1.30x faster                                  |
| spectral_norm            | 96.4 ms                                                | 74.5 ms: 1.29x faster                                  |
| sqlalchemy_imperative    | 9.03 ms                                                | 6.99 ms: 1.29x faster                                  |
| logging_simple           | 4.63 us                                                | 3.59 us: 1.29x faster                                  |
| regex_compile            | 96.6 ms                                                | 76.0 ms: 1.27x faster                                  |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 527 ms: 1.27x faster                                   |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| float                    | 72.3 ms                                                | 57.1 ms: 1.27x faster                                  |
| create_gc_cycles         | 876 us                                                 | 704 us: 1.24x faster                                   |
| generators               | 32.9 ms                                                | 26.5 ms: 1.24x faster                                  |
| pprint_safe_repr         | 609 ms                                                 | 490 ms: 1.24x faster                                   |
| pprint_pformat           | 1.24 sec                                               | 1000 ms: 1.24x faster                                  |
| dulwich_log              | 37.1 ms                                                | 30.0 ms: 1.24x faster                                  |
| fannkuch                 | 317 ms                                                 | 259 ms: 1.22x faster                                   |
| deepcopy                 | 278 us                                                 | 227 us: 1.22x faster                                   |
| 2to3                     | 202 ms                                                 | 169 ms: 1.20x faster                                   |
| mypy2                    | 308 ms                                                 | 259 ms: 1.19x faster                                   |
| docutils                 | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| comprehensions           | 17.7 us                                                | 15.1 us: 1.17x faster                                  |
| scimark_fft              | 232 ms                                                 | 200 ms: 1.16x faster                                   |
| xml_etree_process        | 45.1 ms                                                | 38.8 ms: 1.16x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 2.07 us: 1.15x faster                                  |
| sqlalchemy_declarative   | 74.8 ms                                                | 65.0 ms: 1.15x faster                                  |
| coroutines               | 20.2 ms                                                | 17.5 ms: 1.15x faster                                  |
| bench_thread_pool        | 548 us                                                 | 484 us: 1.13x faster                                   |
| nqueens                  | 68.1 ms                                                | 60.1 ms: 1.13x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 34.1 ms: 1.12x faster                                  |
| regex_v8                 | 17.5 ms                                                | 15.8 ms: 1.11x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.15 ms: 1.10x faster                                  |
| sqlglot_normalize        | 197 ms                                                 | 184 ms: 1.07x faster                                   |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| meteor_contest           | 78.6 ms                                                | 74.3 ms: 1.06x faster                                  |
| unpickle                 | 9.77 us                                                | 9.30 us: 1.05x faster                                  |
| python_startup           | 12.6 ms                                                | 12.1 ms: 1.04x faster                                  |
| mdp                      | 1.67 sec                                               | 1.64 sec: 1.02x faster                                 |
| json                     | 3.10 ms                                                | 3.05 ms: 1.01x faster                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                  |
| telco                    | 3.68 ms                                                | 3.70 ms: 1.00x slower                                  |
| pickle                   | 7.36 us                                                | 7.40 us: 1.01x slower                                  |
| pickle_dict              | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| python_startup_no_site   | 9.73 ms                                                | 9.96 ms: 1.02x slower                                  |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                   |
| xml_etree_generate       | 54.3 ms                                                | 56.0 ms: 1.03x slower                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 75.0 ms: 1.03x slower                                  |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                  |
| regex_effbot             | 2.45 ms                                                | 2.61 ms: 1.07x slower                                  |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.09x slower                                  |
| bench_mp_pool            | 41.0 ms                                                | 46.0 ms: 1.12x slower                                  |
| pathlib                  | 28.8 ms                                                | 33.6 ms: 1.17x slower                                  |
| unpickle_list            | 2.66 us                                                | 3.19 us: 1.20x slower                                  |
| dask                     | 258 ms                                                 | 319 ms: 1.24x slower                                   |
| coverage                 | 40.8 ms                                                | 50.8 ms: 1.24x slower                                  |
| async_generators         | 233 ms                                                 | 308 ms: 1.32x slower                                   |
| Geometric mean           | (ref)                                                  | 1.23x faster                                           |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
