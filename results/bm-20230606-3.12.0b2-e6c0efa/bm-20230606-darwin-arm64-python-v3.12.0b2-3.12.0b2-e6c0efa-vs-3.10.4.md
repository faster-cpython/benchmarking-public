
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b2
- machine: darwin-arm64
- commit hash: e6c0efa
- commit date: 2023-06-06
- overall geometric mean: 1.22x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 171 ms: 1.19x faster                                       |
| docutils       | 1.78 sec                                               | 1.56 sec: 1.15x faster                                     |
| tornado_http   | 91.9 ms                                                | 71.1 ms: 1.29x faster                                      |
| Geometric mean | (ref)                                                  | 1.21x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 68.5 ms: 1.37x faster                                      |
| float          | 72.3 ms                                                | 58.2 ms: 1.24x faster                                      |
| Geometric mean | (ref)                                                  | 1.20x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 74.9 ms: 1.29x faster                                      |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                      |
| regex_dna      | 160 ms                                                 | 150 ms: 1.06x faster                                       |
| regex_effbot   | 2.45 ms                                                | 2.57 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 191 us: 1.49x faster                                       |
| unpickle_pure_python | 203 us                                                 | 146 us: 1.39x faster                                       |
| json_dumps           | 8.38 ms                                                | 6.45 ms: 1.30x faster                                      |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                     |
| xml_etree_process    | 45.1 ms                                                | 38.9 ms: 1.16x faster                                      |
| unpickle             | 9.77 us                                                | 9.21 us: 1.06x faster                                      |
| pickle               | 7.36 us                                                | 7.39 us: 1.00x slower                                      |
| xml_etree_generate   | 54.3 ms                                                | 56.1 ms: 1.03x slower                                      |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.04x slower                                       |
| xml_etree_iterparse  | 72.6 ms                                                | 75.4 ms: 1.04x slower                                      |
| pickle_list          | 2.83 us                                                | 2.94 us: 1.04x slower                                      |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                      |
| unpickle_list        | 2.66 us                                                | 3.16 us: 1.18x slower                                      |
| Geometric mean       | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.0 ms: 1.15x faster                                      |
| python_startup_no_site | 9.73 ms                                                | 8.87 ms: 1.10x faster                                      |
| Geometric mean         | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.55 ms: 1.39x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230606-darwin-arm64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 90.5 us: 3.80x faster                                      |
| deltablue                | 5.15 ms                                                | 2.59 ms: 1.99x faster                                      |
| logging_silent           | 119 ns                                                 | 68.6 ns: 1.74x faster                                      |
| richards_super           | 60.7 ms                                                | 35.3 ms: 1.72x faster                                      |
| richards                 | 51.4 ms                                                | 31.6 ms: 1.63x faster                                      |
| mypy2                    | 308 ms                                                 | 192 ms: 1.61x faster                                       |
| async_tree_memoization   | 493 ms                                                 | 309 ms: 1.60x faster                                       |
| go                       | 165 ms                                                 | 106 ms: 1.55x faster                                       |
| async_tree_none          | 402 ms                                                 | 262 ms: 1.54x faster                                       |
| async_tree_io            | 1.02 sec                                               | 668 ms: 1.53x faster                                       |
| scimark_lu               | 110 ms                                                 | 72.6 ms: 1.51x faster                                      |
| asyncio_tcp              | 673 ms                                                 | 448 ms: 1.50x faster                                       |
| crypto_pyaes             | 78.0 ms                                                | 51.9 ms: 1.50x faster                                      |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.50x faster                                      |
| sqlglot_parse            | 1.33 ms                                                | 894 us: 1.49x faster                                       |
| pickle_pure_python       | 284 us                                                 | 191 us: 1.49x faster                                       |
| chaos                    | 66.8 ms                                                | 45.5 ms: 1.47x faster                                      |
| scimark_monte_carlo      | 72.2 ms                                                | 50.3 ms: 1.44x faster                                      |
| sqlglot_transpile        | 1.54 ms                                                | 1.07 ms: 1.43x faster                                      |
| unpickle_pure_python     | 203 us                                                 | 146 us: 1.39x faster                                       |
| mako                     | 10.5 ms                                                | 7.55 ms: 1.39x faster                                      |
| deepcopy_memo            | 34.5 us                                                | 25.0 us: 1.38x faster                                      |
| pyflate                  | 453 ms                                                 | 330 ms: 1.37x faster                                       |
| nbody                    | 94.1 ms                                                | 68.5 ms: 1.37x faster                                      |
| pycparser                | 915 ms                                                 | 675 ms: 1.36x faster                                       |
| unpack_sequence          | 38.7 ns                                                | 28.8 ns: 1.34x faster                                      |
| scimark_sor              | 127 ms                                                 | 95.4 ms: 1.33x faster                                      |
| raytrace                 | 328 ms                                                 | 248 ms: 1.32x faster                                       |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.25 sec: 1.31x faster                                     |
| json_dumps               | 8.38 ms                                                | 6.45 ms: 1.30x faster                                      |
| tornado_http             | 91.9 ms                                                | 71.1 ms: 1.29x faster                                      |
| spectral_norm            | 96.4 ms                                                | 74.7 ms: 1.29x faster                                      |
| sqlalchemy_imperative    | 9.03 ms                                                | 6.99 ms: 1.29x faster                                      |
| regex_compile            | 96.6 ms                                                | 74.9 ms: 1.29x faster                                      |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 525 ms: 1.28x faster                                       |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                     |
| generators               | 32.9 ms                                                | 26.1 ms: 1.26x faster                                      |
| create_gc_cycles         | 876 us                                                 | 698 us: 1.25x faster                                       |
| logging_format           | 5.01 us                                                | 4.01 us: 1.25x faster                                      |
| logging_simple           | 4.63 us                                                | 3.72 us: 1.24x faster                                      |
| float                    | 72.3 ms                                                | 58.2 ms: 1.24x faster                                      |
| pprint_pformat           | 1.24 sec                                               | 1.01 sec: 1.23x faster                                     |
| deepcopy                 | 278 us                                                 | 226 us: 1.23x faster                                       |
| pprint_safe_repr         | 609 ms                                                 | 497 ms: 1.22x faster                                       |
| dulwich_log              | 37.1 ms                                                | 30.3 ms: 1.22x faster                                      |
| fannkuch                 | 317 ms                                                 | 267 ms: 1.19x faster                                       |
| 2to3                     | 202 ms                                                 | 171 ms: 1.19x faster                                       |
| xml_etree_process        | 45.1 ms                                                | 38.9 ms: 1.16x faster                                      |
| deepcopy_reduce          | 2.38 us                                                | 2.06 us: 1.16x faster                                      |
| scimark_fft              | 232 ms                                                 | 202 ms: 1.15x faster                                       |
| python_startup           | 12.6 ms                                                | 11.0 ms: 1.15x faster                                      |
| sqlalchemy_declarative   | 74.8 ms                                                | 65.3 ms: 1.15x faster                                      |
| docutils                 | 1.78 sec                                               | 1.56 sec: 1.15x faster                                     |
| coroutines               | 20.2 ms                                                | 17.6 ms: 1.14x faster                                      |
| bench_thread_pool        | 548 us                                                 | 484 us: 1.13x faster                                       |
| nqueens                  | 68.1 ms                                                | 61.0 ms: 1.12x faster                                      |
| regex_v8                 | 17.5 ms                                                | 15.8 ms: 1.11x faster                                      |
| sqlglot_optimize         | 38.0 ms                                                | 34.4 ms: 1.11x faster                                      |
| comprehensions           | 17.7 us                                                | 16.1 us: 1.10x faster                                      |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.16 ms: 1.10x faster                                      |
| python_startup_no_site   | 9.73 ms                                                | 8.87 ms: 1.10x faster                                      |
| regex_dna                | 160 ms                                                 | 150 ms: 1.06x faster                                       |
| unpickle                 | 9.77 us                                                | 9.21 us: 1.06x faster                                      |
| sqlglot_normalize        | 197 ms                                                 | 186 ms: 1.06x faster                                       |
| meteor_contest           | 78.6 ms                                                | 74.5 ms: 1.06x faster                                      |
| json                     | 3.10 ms                                                | 3.03 ms: 1.02x faster                                      |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                      |
| pickle                   | 7.36 us                                                | 7.39 us: 1.00x slower                                      |
| telco                    | 3.68 ms                                                | 3.80 ms: 1.03x slower                                      |
| xml_etree_generate       | 54.3 ms                                                | 56.1 ms: 1.03x slower                                      |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.04x slower                                       |
| xml_etree_iterparse      | 72.6 ms                                                | 75.4 ms: 1.04x slower                                      |
| pickle_list              | 2.83 us                                                | 2.94 us: 1.04x slower                                      |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                      |
| regex_effbot             | 2.45 ms                                                | 2.57 ms: 1.05x slower                                      |
| sqlite_synth             | 1.47 us                                                | 1.57 us: 1.06x slower                                      |
| bench_mp_pool            | 41.0 ms                                                | 44.7 ms: 1.09x slower                                      |
| pathlib                  | 28.8 ms                                                | 32.0 ms: 1.11x slower                                      |
| unpickle_list            | 2.66 us                                                | 3.16 us: 1.18x slower                                      |
| coverage                 | 40.8 ms                                                | 50.5 ms: 1.24x slower                                      |
| dask                     | 258 ms                                                 | 328 ms: 1.27x slower                                       |
| async_generators         | 233 ms                                                 | 307 ms: 1.32x slower                                       |
| Geometric mean           | (ref)                                                  | 1.22x faster                                               |

Benchmark hidden because not significant (3): mdp, pickle_dict, pidigits
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
