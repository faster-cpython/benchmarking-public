
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: darwin-arm64
- commit hash: 0e5eee0
- commit date: 2023-08-20
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-darwin-arm64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 168 ms: 1.21x faster                                    |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.19x faster                                  |
| tornado_http   | 91.9 ms                                                | 70.8 ms: 1.30x faster                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-darwin-arm64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.0 ms: 1.36x faster                                   |
| float          | 72.3 ms                                                | 56.5 ms: 1.28x faster                                   |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                    |
| Geometric mean | (ref)                                                  | 1.21x faster                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-darwin-arm64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.6 ms: 1.28x faster                                   |
| regex_v8       | 17.5 ms                                                | 15.6 ms: 1.12x faster                                   |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                    |
| regex_effbot   | 2.45 ms                                                | 2.55 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-darwin-arm64-python-3.12-3.12.0rc1+-0e5eee0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 189 us: 1.50x faster                                    |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                    |
| json_dumps           | 8.38 ms                                                | 6.31 ms: 1.33x faster                                   |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 38.7 ms: 1.17x faster                                   |
| unpickle             | 9.77 us                                                | 9.22 us: 1.06x faster                                   |
| pickle               | 7.36 us                                                | 7.28 us: 1.01x faster                                   |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                   |
| pickle_list          | 2.83 us                                                | 2.86 us: 1.01x slower                                   |
| xml_etree_iterparse  | 72.6 ms                                                | 74.7 ms: 1.03x slower                                   |
| xml_etree_generate   | 54.3 ms                                                | 55.8 ms: 1.03x slower                                   |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                    |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                   |
| unpickle_list        | 2.66 us                                                | 3.19 us: 1.20x slower                                   |
| Geometric mean       | (ref)                                                  | 1.09x faster                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-darwin-arm64-python-3.12-3.12.0rc1+-0e5eee0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.3 ms: 1.11x faster                                   |
| python_startup_no_site | 9.73 ms                                                | 9.19 ms: 1.06x faster                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-darwin-arm64-python-3.12-3.12.0rc1+-0e5eee0 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.62 ms: 1.37x faster                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230820-darwin-arm64-python-3.12-3.12.0rc1+-0e5eee0 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 90.3 us: 3.81x faster                                   |
| deltablue                | 5.15 ms                                                | 2.41 ms: 2.14x faster                                   |
| richards_super           | 60.7 ms                                                | 34.0 ms: 1.78x faster                                   |
| go                       | 165 ms                                                 | 94.0 ms: 1.75x faster                                   |
| logging_silent           | 119 ns                                                 | 68.2 ns: 1.75x faster                                   |
| richards                 | 51.4 ms                                                | 30.4 ms: 1.69x faster                                   |
| scimark_monte_carlo      | 72.2 ms                                                | 43.3 ms: 1.67x faster                                   |
| sqlglot_parse            | 1.33 ms                                                | 829 us: 1.61x faster                                    |
| async_tree_memoization   | 493 ms                                                 | 307 ms: 1.60x faster                                    |
| chaos                    | 66.8 ms                                                | 41.9 ms: 1.59x faster                                   |
| raytrace                 | 328 ms                                                 | 208 ms: 1.58x faster                                    |
| async_tree_io            | 1.02 sec                                               | 653 ms: 1.56x faster                                    |
| async_tree_none          | 402 ms                                                 | 260 ms: 1.55x faster                                    |
| sqlglot_transpile        | 1.54 ms                                                | 1.00 ms: 1.53x faster                                   |
| scimark_lu               | 110 ms                                                 | 72.5 ms: 1.52x faster                                   |
| hexiom                   | 6.32 ms                                                | 4.20 ms: 1.51x faster                                   |
| crypto_pyaes             | 78.0 ms                                                | 51.8 ms: 1.51x faster                                   |
| pickle_pure_python       | 284 us                                                 | 189 us: 1.50x faster                                    |
| scimark_sor              | 127 ms                                                 | 85.5 ms: 1.48x faster                                   |
| pyflate                  | 453 ms                                                 | 307 ms: 1.48x faster                                    |
| asyncio_tcp              | 673 ms                                                 | 467 ms: 1.44x faster                                    |
| unpickle_pure_python     | 203 us                                                 | 145 us: 1.40x faster                                    |
| deepcopy_memo            | 34.5 us                                                | 24.8 us: 1.39x faster                                   |
| mako                     | 10.5 ms                                                | 7.62 ms: 1.37x faster                                   |
| pycparser                | 915 ms                                                 | 667 ms: 1.37x faster                                    |
| nbody                    | 94.1 ms                                                | 69.0 ms: 1.36x faster                                   |
| unpack_sequence          | 38.7 ns                                                | 29.0 ns: 1.33x faster                                   |
| json_dumps               | 8.38 ms                                                | 6.31 ms: 1.33x faster                                   |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.24 sec: 1.33x faster                                  |
| sqlalchemy_imperative    | 9.03 ms                                                | 6.87 ms: 1.32x faster                                   |
| tornado_http             | 91.9 ms                                                | 70.8 ms: 1.30x faster                                   |
| logging_format           | 5.01 us                                                | 3.87 us: 1.30x faster                                   |
| logging_simple           | 4.63 us                                                | 3.58 us: 1.29x faster                                   |
| spectral_norm            | 96.4 ms                                                | 74.6 ms: 1.29x faster                                   |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 520 ms: 1.29x faster                                    |
| float                    | 72.3 ms                                                | 56.5 ms: 1.28x faster                                   |
| regex_compile            | 96.6 ms                                                | 75.6 ms: 1.28x faster                                   |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                  |
| generators               | 32.9 ms                                                | 26.0 ms: 1.27x faster                                   |
| create_gc_cycles         | 876 us                                                 | 699 us: 1.25x faster                                    |
| pprint_pformat           | 1.24 sec                                               | 998 ms: 1.24x faster                                    |
| pprint_safe_repr         | 609 ms                                                 | 490 ms: 1.24x faster                                    |
| deepcopy                 | 278 us                                                 | 224 us: 1.24x faster                                    |
| dulwich_log              | 37.1 ms                                                | 30.1 ms: 1.23x faster                                   |
| mypy2                    | 308 ms                                                 | 255 ms: 1.21x faster                                    |
| 2to3                     | 202 ms                                                 | 168 ms: 1.21x faster                                    |
| fannkuch                 | 317 ms                                                 | 265 ms: 1.20x faster                                    |
| docutils                 | 1.78 sec                                               | 1.49 sec: 1.19x faster                                  |
| comprehensions           | 17.7 us                                                | 14.9 us: 1.18x faster                                   |
| xml_etree_process        | 45.1 ms                                                | 38.7 ms: 1.17x faster                                   |
| scimark_fft              | 232 ms                                                 | 199 ms: 1.16x faster                                    |
| deepcopy_reduce          | 2.38 us                                                | 2.05 us: 1.16x faster                                   |
| coroutines               | 20.2 ms                                                | 17.4 ms: 1.16x faster                                   |
| sqlalchemy_declarative   | 74.8 ms                                                | 64.7 ms: 1.16x faster                                   |
| nqueens                  | 68.1 ms                                                | 59.4 ms: 1.15x faster                                   |
| bench_thread_pool        | 548 us                                                 | 487 us: 1.13x faster                                    |
| regex_v8                 | 17.5 ms                                                | 15.6 ms: 1.12x faster                                   |
| sqlglot_optimize         | 38.0 ms                                                | 34.0 ms: 1.12x faster                                   |
| python_startup           | 12.6 ms                                                | 11.3 ms: 1.11x faster                                   |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.16 ms: 1.10x faster                                   |
| sqlglot_normalize        | 197 ms                                                 | 183 ms: 1.07x faster                                    |
| regex_dna                | 160 ms                                                 | 149 ms: 1.07x faster                                    |
| meteor_contest           | 78.6 ms                                                | 74.0 ms: 1.06x faster                                   |
| unpickle                 | 9.77 us                                                | 9.22 us: 1.06x faster                                   |
| python_startup_no_site   | 9.73 ms                                                | 9.19 ms: 1.06x faster                                   |
| mdp                      | 1.67 sec                                               | 1.63 sec: 1.03x faster                                  |
| json                     | 3.10 ms                                                | 3.03 ms: 1.02x faster                                   |
| pickle                   | 7.36 us                                                | 7.28 us: 1.01x faster                                   |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                    |
| gc_traversal             | 2.40 ms                                                | 2.39 ms: 1.00x faster                                   |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                   |
| pickle_list              | 2.83 us                                                | 2.86 us: 1.01x slower                                   |
| telco                    | 3.68 ms                                                | 3.73 ms: 1.01x slower                                   |
| xml_etree_iterparse      | 72.6 ms                                                | 74.7 ms: 1.03x slower                                   |
| xml_etree_generate       | 54.3 ms                                                | 55.8 ms: 1.03x slower                                   |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                    |
| pathlib                  | 28.8 ms                                                | 29.9 ms: 1.04x slower                                   |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                   |
| regex_effbot             | 2.45 ms                                                | 2.55 ms: 1.04x slower                                   |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.09x slower                                   |
| bench_mp_pool            | 41.0 ms                                                | 45.5 ms: 1.11x slower                                   |
| unpickle_list            | 2.66 us                                                | 3.19 us: 1.20x slower                                   |
| dask                     | 258 ms                                                 | 316 ms: 1.23x slower                                    |
| coverage                 | 40.8 ms                                                | 50.5 ms: 1.24x slower                                   |
| async_generators         | 233 ms                                                 | 307 ms: 1.32x slower                                    |
| Geometric mean           | (ref)                                                  | 1.24x faster                                            |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x
