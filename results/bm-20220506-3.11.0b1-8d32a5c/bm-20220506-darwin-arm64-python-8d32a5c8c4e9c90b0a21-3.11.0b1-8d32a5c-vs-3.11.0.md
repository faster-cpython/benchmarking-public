
# Results vs. 3.11.0

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: darwin-arm64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.00x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 184 ms: 1.14x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.75 ms: 1.04x slower                                                 |
| docutils       | 1.47 sec                                               | 1.45 sec: 1.01x faster                                                |
| html5lib       | 34.7 ms                                                | 33.2 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.4 ms: 1.03x faster                                                 |
| nbody          | 65.5 ms                                                | 64.0 ms: 1.02x faster                                                 |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.03 ms: 1.30x faster                                                 |
| regex_dna      | 152 ms                                                 | 140 ms: 1.08x faster                                                  |
| regex_v8       | 16.2 ms                                                | 15.8 ms: 1.02x faster                                                 |
| regex_compile  | 76.7 ms                                                | 78.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 99.3 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 65.5 ms: 1.06x faster                                                 |
| pickle_dict          | 17.9 us                                                | 17.1 us: 1.04x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.71 us: 1.04x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.61 us: 1.01x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 49.0 ms: 1.00x slower                                                 |
| json_dumps           | 7.72 ms                                                | 7.77 ms: 1.01x slower                                                 |
| xml_etree_process    | 35.2 ms                                                | 35.9 ms: 1.02x slower                                                 |
| json_loads           | 16.1 us                                                | 16.4 us: 1.02x slower                                                 |
| unpickle             | 9.70 us                                                | 9.91 us: 1.02x slower                                                 |
| pickle_pure_python   | 199 us                                                 | 212 us: 1.07x slower                                                  |
| unpickle_pure_python | 159 us                                                 | 181 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.24 ms: 1.29x faster                                                 |
| python_startup         | 11.5 ms                                                | 9.22 ms: 1.25x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.40 ms: 1.01x faster                                                 |
| genshi_text     | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| django_template | 21.0 ms                                                | 21.5 ms: 1.02x slower                                                 |
| genshi_xml      | 29.8 ms                                                | 31.6 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.7 ms: 1.34x faster                                                 |
| regex_effbot            | 2.63 ms                                                | 2.03 ms: 1.30x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 7.24 ms: 1.29x faster                                                 |
| python_startup          | 11.5 ms                                                | 9.22 ms: 1.25x faster                                                 |
| regex_dna               | 152 ms                                                 | 140 ms: 1.08x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 99.3 ms: 1.07x faster                                                 |
| flaskblogging           | 2.42 ms                                                | 2.29 ms: 1.06x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 65.5 ms: 1.06x faster                                                 |
| scimark_sor             | 83.0 ms                                                | 79.2 ms: 1.05x faster                                                 |
| bench_mp_pool           | 43.2 ms                                                | 41.2 ms: 1.05x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.1 us: 1.04x faster                                                 |
| html5lib                | 34.7 ms                                                | 33.2 ms: 1.04x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 32.3 ns: 1.04x faster                                                 |
| pickle_list             | 2.81 us                                                | 2.71 us: 1.04x faster                                                 |
| float                   | 53.0 ms                                                | 51.4 ms: 1.03x faster                                                 |
| sympy_sum               | 86.0 ms                                                | 83.6 ms: 1.03x faster                                                 |
| aiohttp                 | 1.06 ms                                                | 1.03 ms: 1.03x faster                                                 |
| deltablue               | 2.81 ms                                                | 2.74 ms: 1.02x faster                                                 |
| regex_v8                | 16.2 ms                                                | 15.8 ms: 1.02x faster                                                 |
| nqueens                 | 61.8 ms                                                | 60.4 ms: 1.02x faster                                                 |
| nbody                   | 65.5 ms                                                | 64.0 ms: 1.02x faster                                                 |
| spectral_norm           | 72.8 ms                                                | 71.7 ms: 1.01x faster                                                 |
| docutils                | 1.47 sec                                               | 1.45 sec: 1.01x faster                                                |
| dulwich_log             | 29.9 ms                                                | 29.5 ms: 1.01x faster                                                 |
| mako                    | 8.49 ms                                                | 8.40 ms: 1.01x faster                                                 |
| unpickle_list           | 2.63 us                                                | 2.61 us: 1.01x faster                                                 |
| deepcopy                | 224 us                                                 | 222 us: 1.01x faster                                                  |
| logging_silent          | 68.0 ns                                                | 67.5 ns: 1.01x faster                                                 |
| deepcopy_reduce         | 1.91 us                                                | 1.90 us: 1.01x faster                                                 |
| generators              | 28.8 ms                                                | 28.6 ms: 1.01x faster                                                 |
| raytrace                | 207 ms                                                 | 207 ms: 1.00x faster                                                  |
| deepcopy_memo           | 26.3 us                                                | 26.2 us: 1.00x faster                                                 |
| sqlalchemy_declarative  | 62.7 ms                                                | 62.8 ms: 1.00x slower                                                 |
| fannkuch                | 261 ms                                                 | 261 ms: 1.00x slower                                                  |
| xml_etree_generate      | 48.8 ms                                                | 49.0 ms: 1.00x slower                                                 |
| telco                   | 3.39 ms                                                | 3.41 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                                  |
| genshi_text             | 15.3 ms                                                | 15.4 ms: 1.01x slower                                                 |
| async_tree_none         | 285 ms                                                 | 286 ms: 1.01x slower                                                  |
| json_dumps              | 7.72 ms                                                | 7.77 ms: 1.01x slower                                                 |
| crypto_pyaes            | 51.7 ms                                                | 52.1 ms: 1.01x slower                                                 |
| scimark_fft             | 199 ms                                                 | 201 ms: 1.01x slower                                                  |
| sympy_str               | 152 ms                                                 | 153 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.23 ms: 1.01x slower                                                 |
| go                      | 109 ms                                                 | 110 ms: 1.01x slower                                                  |
| pprint_safe_repr        | 465 ms                                                 | 470 ms: 1.01x slower                                                  |
| mdp                     | 1.54 sec                                               | 1.56 sec: 1.01x slower                                                |
| pprint_pformat          | 950 ms                                                 | 966 ms: 1.02x slower                                                  |
| pycparser               | 697 ms                                                 | 709 ms: 1.02x slower                                                  |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.44 ms: 1.02x slower                                                 |
| xml_etree_process       | 35.2 ms                                                | 35.9 ms: 1.02x slower                                                 |
| json_loads              | 16.1 us                                                | 16.4 us: 1.02x slower                                                 |
| bench_thread_pool       | 473 us                                                 | 482 us: 1.02x slower                                                  |
| thrift                  | 433 us                                                 | 443 us: 1.02x slower                                                  |
| django_template         | 21.0 ms                                                | 21.5 ms: 1.02x slower                                                 |
| regex_compile           | 76.7 ms                                                | 78.4 ms: 1.02x slower                                                 |
| unpickle                | 9.70 us                                                | 9.91 us: 1.02x slower                                                 |
| chaos                   | 49.5 ms                                                | 50.6 ms: 1.02x slower                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.02x slower                                                 |
| sympy_expand            | 243 ms                                                 | 249 ms: 1.02x slower                                                  |
| scimark_lu              | 72.1 ms                                                | 73.7 ms: 1.02x slower                                                 |
| async_generators        | 195 ms                                                 | 200 ms: 1.03x slower                                                  |
| logging_simple          | 3.50 us                                                | 3.60 us: 1.03x slower                                                 |
| logging_format          | 3.78 us                                                | 3.90 us: 1.03x slower                                                 |
| pyflate                 | 311 ms                                                 | 322 ms: 1.03x slower                                                  |
| chameleon               | 4.57 ms                                                | 4.75 ms: 1.04x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.32 us: 1.04x slower                                                 |
| hexiom                  | 4.73 ms                                                | 4.92 ms: 1.04x slower                                                 |
| meteor_contest          | 73.8 ms                                                | 76.8 ms: 1.04x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 179 ms: 1.05x slower                                                  |
| richards                | 32.2 ms                                                | 33.8 ms: 1.05x slower                                                 |
| json                    | 2.77 ms                                                | 2.92 ms: 1.05x slower                                                 |
| scimark_monte_carlo     | 46.4 ms                                                | 48.9 ms: 1.05x slower                                                 |
| sqlglot_optimize        | 31.2 ms                                                | 33.0 ms: 1.06x slower                                                 |
| coroutines              | 17.7 ms                                                | 18.8 ms: 1.06x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 31.6 ms: 1.06x slower                                                 |
| async_tree_memoization  | 336 ms                                                 | 356 ms: 1.06x slower                                                  |
| pickle_pure_python      | 199 us                                                 | 212 us: 1.07x slower                                                  |
| unpickle_pure_python    | 159 us                                                 | 181 us: 1.14x slower                                                  |
| 2to3                    | 161 ms                                                 | 184 ms: 1.14x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.38 ms: 1.23x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.21 ms: 1.26x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (6): tornado_http, pylint, async_tree_io, async_tree_cpu_io_mixed, pickle, gunicorn
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp, comprehensions, coverage, create_gc_cycles, dask, gc_traversal, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220506-3.11.0b1-8d32a5c/bm-20220506-darwin-arm64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c.json: mypy
