
# Results vs. 3.10.4

- fork: python
- ref: 2e91dba437fe5c56c6f8
- machine: darwin-arm64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 168 ms: 1.20x faster                                                  |
| chameleon      | 5.79 ms                                                | 5.16 ms: 1.12x faster                                                 |
| docutils       | 1.78 sec                                               | 1.57 sec: 1.14x faster                                                |
| html5lib       | 44.2 ms                                                | 37.0 ms: 1.19x faster                                                 |
| tornado_http   | 91.5 ms                                                | 79.1 ms: 1.16x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.3 ms: 1.43x faster                                                 |
| float          | 72.4 ms                                                | 56.7 ms: 1.28x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 78.8 ms: 1.22x faster                                                 |
| regex_v8       | 17.6 ms                                                | 17.1 ms: 1.03x faster                                                 |
| regex_dna      | 162 ms                                                 | 159 ms: 1.01x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 224 us: 1.27x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 37.7 ms: 1.19x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 176 us: 1.15x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 50.3 ms: 1.08x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 99.0 ms: 1.08x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.51 us: 1.07x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.99 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 70.1 ms: 1.03x faster                                                 |
| json_loads           | 16.9 us                                                | 16.6 us: 1.02x faster                                                 |
| pickle_list          | 2.80 us                                                | 2.82 us: 1.01x slower                                                 |
| pickle               | 7.35 us                                                | 7.42 us: 1.01x slower                                                 |
| unpickle             | 9.89 us                                                | 10.1 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.88 ms                                                | 9.23 ms: 1.04x slower                                                 |
| python_startup         | 11.9 ms                                                | 15.4 ms: 1.29x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.53 ms: 1.23x faster                                                 |
| django_template | 27.3 ms                                                | 22.9 ms: 1.19x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 32.3 ms: 1.15x faster                                                 |
| genshi_text     | 18.4 ms                                                | 16.3 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 3.10 ms: 1.66x faster                                                 |
| logging_silent          | 119 ns                                                 | 81.6 ns: 1.46x faster                                                 |
| scimark_sor             | 126 ms                                                 | 86.2 ms: 1.46x faster                                                 |
| raytrace                | 325 ms                                                 | 227 ms: 1.43x faster                                                  |
| nbody                   | 93.3 ms                                                | 65.3 ms: 1.43x faster                                                 |
| richards                | 51.4 ms                                                | 36.2 ms: 1.42x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 51.4 ms: 1.41x faster                                                 |
| go                      | 165 ms                                                 | 119 ms: 1.39x faster                                                  |
| scimark_lu              | 109 ms                                                 | 78.6 ms: 1.39x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.70 ms: 1.34x faster                                                 |
| chaos                   | 66.7 ms                                                | 50.3 ms: 1.33x faster                                                 |
| logging_simple          | 4.63 us                                                | 3.52 us: 1.31x faster                                                 |
| async_tree_none         | 400 ms                                                 | 305 ms: 1.31x faster                                                  |
| pyflate                 | 453 ms                                                 | 346 ms: 1.31x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 59.7 ms: 1.31x faster                                                 |
| logging_format          | 4.97 us                                                | 3.83 us: 1.30x faster                                                 |
| float                   | 72.4 ms                                                | 56.7 ms: 1.28x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 224 us: 1.27x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 76.8 ms: 1.25x faster                                                 |
| thrift                  | 580 us                                                 | 470 us: 1.23x faster                                                  |
| mako                    | 10.5 ms                                                | 8.53 ms: 1.23x faster                                                 |
| async_tree_memoization  | 490 ms                                                 | 400 ms: 1.23x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 28.1 us: 1.22x faster                                                 |
| regex_compile           | 96.4 ms                                                | 78.8 ms: 1.22x faster                                                 |
| generators              | 32.7 ms                                                | 27.1 ms: 1.21x faster                                                 |
| pycparser               | 916 ms                                                 | 759 ms: 1.21x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 733 us: 1.20x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 505 ms: 1.20x faster                                                  |
| 2to3                    | 201 ms                                                 | 168 ms: 1.20x faster                                                  |
| html5lib                | 44.2 ms                                                | 37.0 ms: 1.19x faster                                                 |
| django_template         | 27.3 ms                                                | 22.9 ms: 1.19x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 1.03 sec: 1.19x faster                                                |
| async_tree_io           | 1.02 sec                                               | 855 ms: 1.19x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 37.7 ms: 1.19x faster                                                 |
| async_generators        | 234 ms                                                 | 198 ms: 1.18x faster                                                  |
| fannkuch                | 317 ms                                                 | 270 ms: 1.17x faster                                                  |
| deepcopy                | 281 us                                                 | 240 us: 1.17x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 32.0 ns: 1.17x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 31.8 ms: 1.16x faster                                                 |
| deepcopy_reduce         | 2.37 us                                                | 2.04 us: 1.16x faster                                                 |
| tornado_http            | 91.5 ms                                                | 79.1 ms: 1.16x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 176 us: 1.15x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 32.3 ms: 1.15x faster                                                 |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.80 ms: 1.14x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 587 ms: 1.14x faster                                                  |
| scimark_fft             | 230 ms                                                 | 202 ms: 1.14x faster                                                  |
| docutils                | 1.78 sec                                               | 1.57 sec: 1.14x faster                                                |
| genshi_text             | 18.4 ms                                                | 16.3 ms: 1.13x faster                                                 |
| chameleon               | 5.79 ms                                                | 5.16 ms: 1.12x faster                                                 |
| nqueens                 | 68.2 ms                                                | 61.1 ms: 1.12x faster                                                 |
| sqlalchemy_declarative  | 74.9 ms                                                | 67.3 ms: 1.11x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 34.4 ms: 1.10x faster                                                 |
| sqlglot_normalize       | 196 ms                                                 | 179 ms: 1.09x faster                                                  |
| sympy_integrate         | 13.3 ms                                                | 12.1 ms: 1.09x faster                                                 |
| coroutines              | 20.2 ms                                                | 18.6 ms: 1.09x faster                                                 |
| flaskblogging           | 2.75 ms                                                | 2.54 ms: 1.08x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.37 us: 1.08x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 50.3 ms: 1.08x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 99.0 ms: 1.08x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.47 ms: 1.07x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.51 us: 1.07x faster                                                 |
| pylint                  | 307 ms                                                 | 287 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.26 ms: 1.06x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 73.7 ms: 1.06x faster                                                 |
| sqlglot_parse           | 1.37 ms                                                | 1.29 ms: 1.06x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 517 us: 1.06x faster                                                  |
| sympy_expand            | 275 ms                                                 | 261 ms: 1.06x faster                                                  |
| json_dumps              | 8.40 ms                                                | 7.99 ms: 1.05x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.58 sec: 1.05x faster                                                |
| pathlib                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                 |
| sympy_str               | 169 ms                                                 | 162 ms: 1.05x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 89.6 ms: 1.05x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 70.1 ms: 1.03x faster                                                 |
| json                    | 3.08 ms                                                | 2.99 ms: 1.03x faster                                                 |
| regex_v8                | 17.6 ms                                                | 17.1 ms: 1.03x faster                                                 |
| dask                    | 265 ms                                                 | 258 ms: 1.03x faster                                                  |
| json_loads              | 16.9 us                                                | 16.6 us: 1.02x faster                                                 |
| telco                   | 3.63 ms                                                | 3.57 ms: 1.02x faster                                                 |
| regex_dna               | 162 ms                                                 | 159 ms: 1.01x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_effbot            | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.82 us: 1.01x slower                                                 |
| pickle                  | 7.35 us                                                | 7.42 us: 1.01x slower                                                 |
| gc_traversal            | 2.39 ms                                                | 2.43 ms: 1.02x slower                                                 |
| unpickle                | 9.89 us                                                | 10.1 us: 1.02x slower                                                 |
| comprehensions          | 17.6 us                                                | 18.0 us: 1.02x slower                                                 |
| python_startup_no_site  | 8.88 ms                                                | 9.23 ms: 1.04x slower                                                 |
| coverage                | 42.0 ms                                                | 45.6 ms: 1.08x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 43.8 ms: 1.10x slower                                                 |
| python_startup          | 11.9 ms                                                | 15.4 ms: 1.29x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, gunicorn, mypy2
