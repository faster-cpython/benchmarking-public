
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3a5be87
- commit date: 2023-05-28
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| html5lib       | 34.7 ms                                                | 37.4 ms: 1.08x slower                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 281 ms                                                 | 281 ms: 1.00x faster                                  |
| nbody          | 65.6 ms                                                | 67.7 ms: 1.03x slower                                 |
| float          | 53.0 ms                                                | 58.9 ms: 1.11x slower                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 151 ms: 1.01x faster                                  |
| regex_v8       | 16.1 ms                                                | 16.2 ms: 1.01x slower                                 |
| regex_compile  | 76.7 ms                                                | 79.1 ms: 1.03x slower                                 |
| regex_effbot   | 2.63 ms                                                | 2.71 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.91 ms: 1.10x faster                                 |
| unpickle_pure_python | 159 us                                                 | 153 us: 1.04x faster                                  |
| pickle_pure_python   | 201 us                                                 | 195 us: 1.03x faster                                  |
| tomli_loads          | 1.47 sec                                               | 1.49 sec: 1.02x slower                                |
| unpickle             | 9.67 us                                                | 9.94 us: 1.03x slower                                 |
| pickle_dict          | 18.0 us                                                | 18.8 us: 1.05x slower                                 |
| pickle_list          | 2.81 us                                                | 3.01 us: 1.07x slower                                 |
| xml_etree_iterparse  | 70.1 ms                                                | 75.5 ms: 1.08x slower                                 |
| pickle               | 7.15 us                                                | 7.86 us: 1.10x slower                                 |
| json_loads           | 16.1 us                                                | 17.9 us: 1.11x slower                                 |
| xml_etree_process    | 35.1 ms                                                | 40.5 ms: 1.16x slower                                 |
| unpickle_list        | 2.65 us                                                | 3.16 us: 1.19x slower                                 |
| xml_etree_generate   | 48.3 ms                                                | 58.1 ms: 1.20x slower                                 |
| Geometric mean       | (ref)                                                  | 1.06x slower                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 11.1 ms: 1.12x faster                                 |
| python_startup_no_site | 10.2 ms                                                | 9.16 ms: 1.11x faster                                 |
| Geometric mean         | (ref)                                                  | 1.11x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako           | 8.53 ms                                                | 7.69 ms: 1.11x faster                                 |
| genshi_xml     | 29.8 ms                                                | 31.4 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                 | 91.7 us: 3.66x faster                                 |
| asyncio_tcp              | 651 ms                                                 | 462 ms: 1.41x faster                                  |
| unpack_sequence          | 34.1 ns                                                | 28.6 ns: 1.19x faster                                 |
| asyncio_tcp_ssl          | 1.44 sec                                               | 1.26 sec: 1.15x faster                                |
| deltablue                | 2.81 ms                                                | 2.49 ms: 1.13x faster                                 |
| python_startup           | 12.4 ms                                                | 11.1 ms: 1.12x faster                                 |
| generators               | 28.8 ms                                                | 25.9 ms: 1.11x faster                                 |
| python_startup_no_site   | 10.2 ms                                                | 9.16 ms: 1.11x faster                                 |
| mako                     | 8.53 ms                                                | 7.69 ms: 1.11x faster                                 |
| json_dumps               | 7.63 ms                                                | 6.91 ms: 1.10x faster                                 |
| hexiom                   | 4.72 ms                                                | 4.35 ms: 1.08x faster                                 |
| sqlglot_parse            | 959 us                                                 | 910 us: 1.05x faster                                  |
| richards_super           | 39.2 ms                                                | 37.3 ms: 1.05x faster                                 |
| chaos                    | 49.4 ms                                                | 47.4 ms: 1.04x faster                                 |
| unpickle_pure_python     | 159 us                                                 | 153 us: 1.04x faster                                  |
| sqlglot_transpile        | 1.12 ms                                                | 1.09 ms: 1.03x faster                                 |
| pickle_pure_python       | 201 us                                                 | 195 us: 1.03x faster                                  |
| create_gc_cycles         | 716 us                                                 | 698 us: 1.03x faster                                  |
| deepcopy_memo            | 26.3 us                                                | 25.8 us: 1.02x faster                                 |
| coverage                 | 58.4 ms                                                | 57.6 ms: 1.01x faster                                 |
| regex_dna                | 152 ms                                                 | 151 ms: 1.01x faster                                  |
| async_tree_none          | 286 ms                                                 | 283 ms: 1.01x faster                                  |
| pidigits                 | 281 ms                                                 | 281 ms: 1.00x faster                                  |
| gc_traversal             | 2.42 ms                                                | 2.42 ms: 1.00x slower                                 |
| meteor_contest           | 73.5 ms                                                | 73.8 ms: 1.00x slower                                 |
| regex_v8                 | 16.1 ms                                                | 16.2 ms: 1.01x slower                                 |
| comprehensions           | 16.1 us                                                | 16.3 us: 1.01x slower                                 |
| async_tree_io            | 704 ms                                                 | 712 ms: 1.01x slower                                  |
| mdp                      | 1.55 sec                                               | 1.56 sec: 1.01x slower                                |
| tomli_loads              | 1.47 sec                                               | 1.49 sec: 1.02x slower                                |
| go                       | 109 ms                                                 | 111 ms: 1.02x slower                                  |
| dulwich_log              | 30.3 ms                                                | 30.9 ms: 1.02x slower                                 |
| unpickle                 | 9.67 us                                                | 9.94 us: 1.03x slower                                 |
| coroutines               | 17.8 ms                                                | 18.3 ms: 1.03x slower                                 |
| scimark_sor              | 82.6 ms                                                | 85.0 ms: 1.03x slower                                 |
| richards                 | 32.2 ms                                                | 33.2 ms: 1.03x slower                                 |
| async_tree_cpu_io_mixed  | 533 ms                                                 | 549 ms: 1.03x slower                                  |
| regex_compile            | 76.7 ms                                                | 79.1 ms: 1.03x slower                                 |
| regex_effbot             | 2.63 ms                                                | 2.71 ms: 1.03x slower                                 |
| nbody                    | 65.6 ms                                                | 67.7 ms: 1.03x slower                                 |
| scimark_sparse_mat_mult  | 3.19 ms                                                | 3.30 ms: 1.03x slower                                 |
| logging_silent           | 68.1 ns                                                | 70.7 ns: 1.04x slower                                 |
| scimark_fft              | 200 ms                                                 | 207 ms: 1.04x slower                                  |
| bench_mp_pool            | 43.9 ms                                                | 45.8 ms: 1.04x slower                                 |
| pickle_dict              | 18.0 us                                                | 18.8 us: 1.05x slower                                 |
| genshi_xml               | 29.8 ms                                                | 31.4 ms: 1.05x slower                                 |
| fannkuch                 | 261 ms                                                 | 276 ms: 1.06x slower                                  |
| bench_thread_pool        | 474 us                                                 | 502 us: 1.06x slower                                  |
| logging_simple           | 3.55 us                                                | 3.75 us: 1.06x slower                                 |
| nqueens                  | 59.8 ms                                                | 63.4 ms: 1.06x slower                                 |
| crypto_pyaes             | 51.7 ms                                                | 54.9 ms: 1.06x slower                                 |
| deepcopy                 | 223 us                                                 | 237 us: 1.06x slower                                  |
| docutils                 | 1.47 sec                                               | 1.57 sec: 1.07x slower                                |
| logging_format           | 3.78 us                                                | 4.04 us: 1.07x slower                                 |
| pathlib                  | 27.2 ms                                                | 29.2 ms: 1.07x slower                                 |
| pickle_list              | 2.81 us                                                | 3.01 us: 1.07x slower                                 |
| xml_etree_iterparse      | 70.1 ms                                                | 75.5 ms: 1.08x slower                                 |
| html5lib                 | 34.7 ms                                                | 37.4 ms: 1.08x slower                                 |
| scimark_lu               | 73.3 ms                                                | 79.2 ms: 1.08x slower                                 |
| spectral_norm            | 72.6 ms                                                | 78.7 ms: 1.08x slower                                 |
| pprint_pformat           | 954 ms                                                 | 1.04 sec: 1.09x slower                                |
| json                     | 2.78 ms                                                | 3.05 ms: 1.10x slower                                 |
| pprint_safe_repr         | 466 ms                                                 | 512 ms: 1.10x slower                                  |
| pickle                   | 7.15 us                                                | 7.86 us: 1.10x slower                                 |
| json_loads               | 16.1 us                                                | 17.9 us: 1.11x slower                                 |
| pyflate                  | 310 ms                                                 | 345 ms: 1.11x slower                                  |
| float                    | 53.0 ms                                                | 58.9 ms: 1.11x slower                                 |
| deepcopy_reduce          | 1.91 us                                                | 2.15 us: 1.13x slower                                 |
| scimark_monte_carlo      | 46.5 ms                                                | 52.4 ms: 1.13x slower                                 |
| sqlglot_normalize        | 171 ms                                                 | 194 ms: 1.14x slower                                  |
| xml_etree_process        | 35.1 ms                                                | 40.5 ms: 1.16x slower                                 |
| sqlglot_optimize         | 31.1 ms                                                | 36.0 ms: 1.16x slower                                 |
| unpickle_list            | 2.65 us                                                | 3.16 us: 1.19x slower                                 |
| telco                    | 3.41 ms                                                | 4.10 ms: 1.20x slower                                 |
| xml_etree_generate       | 48.3 ms                                                | 58.1 ms: 1.20x slower                                 |
| raytrace                 | 207 ms                                                 | 250 ms: 1.21x slower                                  |
| sqlite_synth             | 1.27 us                                                | 1.59 us: 1.25x slower                                 |
| mypy2                    | 195 ms                                                 | 265 ms: 1.36x slower                                  |
| async_generators         | 196 ms                                                 | 324 ms: 1.65x slower                                  |
| Geometric mean           | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (5): async_tree_memoization, xml_etree_parse, genshi_text, tornado_http, pycparser
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
