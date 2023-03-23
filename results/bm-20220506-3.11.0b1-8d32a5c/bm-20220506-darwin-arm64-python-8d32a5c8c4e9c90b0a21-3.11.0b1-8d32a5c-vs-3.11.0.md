
# Results vs. 3.11.0

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: darwin-arm64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 162 ms: 1.01x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.64 ms: 1.01x slower                                                 |
| docutils       | 1.47 sec                                               | 1.44 sec: 1.02x faster                                                |
| html5lib       | 34.7 ms                                                | 33.8 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 64.1 ms: 1.02x faster                                                 |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| float          | 53.0 ms                                                | 54.1 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.06 ms: 1.27x faster                                                 |
| regex_v8       | 16.2 ms                                                | 15.1 ms: 1.07x faster                                                 |
| regex_dna      | 152 ms                                                 | 142 ms: 1.07x faster                                                  |
| regex_compile  | 76.7 ms                                                | 77.9 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.74 us: 1.02x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 48.6 ms: 1.00x faster                                                 |
| json_dumps           | 7.72 ms                                                | 7.69 ms: 1.00x faster                                                 |
| xml_etree_process    | 35.2 ms                                                | 35.5 ms: 1.01x slower                                                 |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| unpickle             | 9.70 us                                                | 9.90 us: 1.02x slower                                                 |
| pickle_pure_python   | 199 us                                                 | 219 us: 1.10x slower                                                  |
| unpickle_pure_python | 159 us                                                 | 179 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                | 12.1 ms: 1.05x slower                                                 |
| python_startup_no_site | 9.31 ms                                                | 9.86 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.45 ms: 1.01x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 30.6 ms: 1.03x slower                                                 |
| django_template | 21.0 ms                                                | 21.7 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                | 2.06 ms: 1.27x faster                                                 |
| scimark_sor             | 83.0 ms                                                | 76.6 ms: 1.08x faster                                                 |
| regex_v8                | 16.2 ms                                                | 15.1 ms: 1.07x faster                                                 |
| regex_dna               | 152 ms                                                 | 142 ms: 1.07x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.69 ms: 1.04x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 32.4 ns: 1.04x faster                                                 |
| go                      | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| generators              | 28.8 ms                                                | 28.1 ms: 1.03x faster                                                 |
| html5lib                | 34.7 ms                                                | 33.8 ms: 1.03x faster                                                 |
| pathlib                 | 27.8 ms                                                | 27.1 ms: 1.03x faster                                                 |
| pickle_list             | 2.81 us                                                | 2.74 us: 1.02x faster                                                 |
| nbody                   | 65.5 ms                                                | 64.1 ms: 1.02x faster                                                 |
| docutils                | 1.47 sec                                               | 1.44 sec: 1.02x faster                                                |
| sympy_sum               | 86.0 ms                                                | 84.6 ms: 1.02x faster                                                 |
| spectral_norm           | 72.8 ms                                                | 71.7 ms: 1.01x faster                                                 |
| raytrace                | 207 ms                                                 | 205 ms: 1.01x faster                                                  |
| gc_traversal            | 2.43 ms                                                | 2.41 ms: 1.01x faster                                                 |
| mako                    | 8.49 ms                                                | 8.45 ms: 1.01x faster                                                 |
| create_gc_cycles        | 726 us                                                 | 723 us: 1.00x faster                                                  |
| xml_etree_generate      | 48.8 ms                                                | 48.6 ms: 1.00x faster                                                 |
| json_dumps              | 7.72 ms                                                | 7.69 ms: 1.00x faster                                                 |
| sqlalchemy_declarative  | 62.7 ms                                                | 62.5 ms: 1.00x faster                                                 |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                                  |
| async_tree_io           | 706 ms                                                 | 710 ms: 1.01x slower                                                  |
| 2to3                    | 161 ms                                                 | 162 ms: 1.01x slower                                                  |
| logging_format          | 3.78 us                                                | 3.80 us: 1.01x slower                                                 |
| genshi_text             | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| scimark_fft             | 199 ms                                                 | 201 ms: 1.01x slower                                                  |
| xml_etree_process       | 35.2 ms                                                | 35.5 ms: 1.01x slower                                                 |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.38 ms: 1.01x slower                                                 |
| mdp                     | 1.54 sec                                               | 1.56 sec: 1.01x slower                                                |
| flaskblogging           | 2.42 ms                                                | 2.44 ms: 1.01x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 52.3 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                 | 542 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.24 ms: 1.01x slower                                                 |
| chaos                   | 49.5 ms                                                | 50.1 ms: 1.01x slower                                                 |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                                 |
| chameleon               | 4.57 ms                                                | 4.64 ms: 1.01x slower                                                 |
| regex_compile           | 76.7 ms                                                | 77.9 ms: 1.02x slower                                                 |
| fannkuch                | 261 ms                                                 | 265 ms: 1.02x slower                                                  |
| coroutines              | 17.7 ms                                                | 18.0 ms: 1.02x slower                                                 |
| hexiom                  | 4.73 ms                                                | 4.82 ms: 1.02x slower                                                 |
| sympy_str               | 152 ms                                                 | 154 ms: 1.02x slower                                                  |
| pycparser               | 697 ms                                                 | 710 ms: 1.02x slower                                                  |
| float                   | 53.0 ms                                                | 54.1 ms: 1.02x slower                                                 |
| unpickle                | 9.70 us                                                | 9.90 us: 1.02x slower                                                 |
| thrift                  | 433 us                                                 | 443 us: 1.02x slower                                                  |
| dulwich_log             | 29.9 ms                                                | 30.5 ms: 1.02x slower                                                 |
| dask                    | 226 ms                                                 | 232 ms: 1.02x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.8 ms: 1.02x slower                                                 |
| async_tree_none         | 285 ms                                                 | 292 ms: 1.03x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 30.6 ms: 1.03x slower                                                 |
| sympy_expand            | 243 ms                                                 | 250 ms: 1.03x slower                                                  |
| json                    | 2.77 ms                                                | 2.85 ms: 1.03x slower                                                 |
| async_generators        | 195 ms                                                 | 200 ms: 1.03x slower                                                  |
| sqlglot_normalize       | 171 ms                                                 | 176 ms: 1.03x slower                                                  |
| pyflate                 | 311 ms                                                 | 320 ms: 1.03x slower                                                  |
| django_template         | 21.0 ms                                                | 21.7 ms: 1.03x slower                                                 |
| meteor_contest          | 73.8 ms                                                | 76.6 ms: 1.04x slower                                                 |
| logging_silent          | 68.0 ns                                                | 70.7 ns: 1.04x slower                                                 |
| sqlglot_optimize        | 31.2 ms                                                | 32.4 ms: 1.04x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.34 us: 1.05x slower                                                 |
| python_startup          | 11.5 ms                                                | 12.1 ms: 1.05x slower                                                 |
| bench_thread_pool       | 473 us                                                 | 499 us: 1.05x slower                                                  |
| python_startup_no_site  | 9.31 ms                                                | 9.86 ms: 1.06x slower                                                 |
| scimark_monte_carlo     | 46.4 ms                                                | 49.3 ms: 1.06x slower                                                 |
| async_tree_memoization  | 336 ms                                                 | 357 ms: 1.06x slower                                                  |
| richards                | 32.2 ms                                                | 34.3 ms: 1.06x slower                                                 |
| pprint_safe_repr        | 465 ms                                                 | 499 ms: 1.07x slower                                                  |
| pprint_pformat          | 950 ms                                                 | 1.03 sec: 1.08x slower                                                |
| deepcopy                | 224 us                                                 | 244 us: 1.09x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.11 us: 1.10x slower                                                 |
| pickle_pure_python      | 199 us                                                 | 219 us: 1.10x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 29.1 us: 1.11x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 179 us: 1.13x slower                                                  |
| comprehensions          | 16.1 us                                                | 19.2 us: 1.20x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.38 ms: 1.23x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.21 ms: 1.27x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (15): tornado_http, nqueens, xml_etree_parse, xml_etree_iterparse, telco, asyncio_tcp, pickle, aiohttp, unpickle_list, logging_simple, scimark_lu, mypy2, bench_mp_pool, pylint, gunicorn
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: coverage
