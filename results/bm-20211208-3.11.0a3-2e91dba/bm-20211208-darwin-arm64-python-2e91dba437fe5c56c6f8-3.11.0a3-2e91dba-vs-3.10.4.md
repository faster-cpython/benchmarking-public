
# Results vs. 3.10.4

- fork: python
- ref: 2e91dba437fe5c56c6f8
- machine: darwin-arm64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.16x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| chameleon      | 5.79 ms                                                | 5.14 ms: 1.13x faster                                                 |
| docutils       | 1.78 sec                                               | 1.56 sec: 1.14x faster                                                |
| html5lib       | 44.2 ms                                                | 36.9 ms: 1.20x faster                                                 |
| tornado_http   | 91.5 ms                                                | 79.7 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.2 ms: 1.43x faster                                                 |
| float          | 72.4 ms                                                | 56.5 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 78.4 ms: 1.23x faster                                                 |
| regex_dna      | 162 ms                                                 | 163 ms: 1.01x slower                                                  |
| regex_effbot   | 2.46 ms                                                | 2.50 ms: 1.02x slower                                                 |
| regex_v8       | 17.6 ms                                                | 18.0 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 224 us: 1.27x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 37.5 ms: 1.19x faster                                                 |
| unpickle_pure_python | 203 us                                                 | 177 us: 1.15x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 96.5 ms: 1.10x faster                                                 |
| xml_etree_generate   | 54.2 ms                                                | 49.9 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 72.3 ms                                                | 67.2 ms: 1.07x faster                                                 |
| unpickle_list        | 2.69 us                                                | 2.50 us: 1.07x faster                                                 |
| json_dumps           | 8.40 ms                                                | 7.91 ms: 1.06x faster                                                 |
| json_loads           | 16.9 us                                                | 16.8 us: 1.01x faster                                                 |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| pickle               | 7.35 us                                                | 7.42 us: 1.01x slower                                                 |
| pickle_list          | 2.80 us                                                | 2.85 us: 1.02x slower                                                 |
| unpickle             | 9.89 us                                                | 10.1 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 8.88 ms                                                | 6.93 ms: 1.28x faster                                                 |
| python_startup         | 11.9 ms                                                | 12.7 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 8.53 ms: 1.23x faster                                                 |
| django_template | 27.3 ms                                                | 23.1 ms: 1.18x faster                                                 |
| genshi_xml      | 37.2 ms                                                | 32.4 ms: 1.15x faster                                                 |
| genshi_text     | 18.4 ms                                                | 16.1 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-darwin-arm64-python-2e91dba437fe5c56c6f8-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 3.12 ms: 1.65x faster                                                 |
| logging_silent          | 119 ns                                                 | 81.8 ns: 1.46x faster                                                 |
| scimark_sor             | 126 ms                                                 | 86.7 ms: 1.45x faster                                                 |
| nbody                   | 93.3 ms                                                | 65.2 ms: 1.43x faster                                                 |
| raytrace                | 325 ms                                                 | 228 ms: 1.43x faster                                                  |
| richards                | 51.4 ms                                                | 36.4 ms: 1.41x faster                                                 |
| scimark_monte_carlo     | 72.5 ms                                                | 51.6 ms: 1.41x faster                                                 |
| go                      | 165 ms                                                 | 119 ms: 1.40x faster                                                  |
| scimark_lu              | 109 ms                                                 | 78.9 ms: 1.38x faster                                                 |
| pathlib                 | 28.8 ms                                                | 21.1 ms: 1.37x faster                                                 |
| chaos                   | 66.7 ms                                                | 49.8 ms: 1.34x faster                                                 |
| hexiom                  | 6.32 ms                                                | 4.74 ms: 1.33x faster                                                 |
| async_tree_none         | 400 ms                                                 | 301 ms: 1.33x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.51 us: 1.32x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 59.6 ms: 1.31x faster                                                 |
| pyflate                 | 453 ms                                                 | 347 ms: 1.31x faster                                                  |
| logging_format          | 4.97 us                                                | 3.83 us: 1.30x faster                                                 |
| float                   | 72.4 ms                                                | 56.5 ms: 1.28x faster                                                 |
| python_startup_no_site  | 8.88 ms                                                | 6.93 ms: 1.28x faster                                                 |
| pickle_pure_python      | 283 us                                                 | 224 us: 1.27x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 391 ms: 1.25x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 76.7 ms: 1.25x faster                                                 |
| deepcopy_memo           | 34.4 us                                                | 27.9 us: 1.23x faster                                                 |
| regex_compile           | 96.4 ms                                                | 78.4 ms: 1.23x faster                                                 |
| mako                    | 10.5 ms                                                | 8.53 ms: 1.23x faster                                                 |
| thrift                  | 580 us                                                 | 474 us: 1.23x faster                                                  |
| async_tree_io           | 1.02 sec                                               | 833 ms: 1.22x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 503 ms: 1.20x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 30.8 ms: 1.20x faster                                                 |
| pycparser               | 916 ms                                                 | 762 ms: 1.20x faster                                                  |
| generators              | 32.7 ms                                                | 27.3 ms: 1.20x faster                                                 |
| html5lib                | 44.2 ms                                                | 36.9 ms: 1.20x faster                                                 |
| pprint_pformat          | 1.23 sec                                               | 1.03 sec: 1.20x faster                                                |
| xml_etree_process       | 44.8 ms                                                | 37.5 ms: 1.19x faster                                                 |
| async_generators        | 234 ms                                                 | 197 ms: 1.19x faster                                                  |
| fannkuch                | 317 ms                                                 | 269 ms: 1.18x faster                                                  |
| django_template         | 27.3 ms                                                | 23.1 ms: 1.18x faster                                                 |
| deepcopy                | 281 us                                                 | 240 us: 1.17x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 32.2 ns: 1.16x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 580 ms: 1.15x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 2.06 us: 1.15x faster                                                 |
| unpickle_pure_python    | 203 us                                                 | 177 us: 1.15x faster                                                  |
| tornado_http            | 91.5 ms                                                | 79.7 ms: 1.15x faster                                                 |
| genshi_xml              | 37.2 ms                                                | 32.4 ms: 1.15x faster                                                 |
| docutils                | 1.78 sec                                               | 1.56 sec: 1.14x faster                                                |
| genshi_text             | 18.4 ms                                                | 16.1 ms: 1.14x faster                                                 |
| scimark_fft             | 230 ms                                                 | 202 ms: 1.14x faster                                                  |
| chameleon               | 5.79 ms                                                | 5.14 ms: 1.13x faster                                                 |
| nqueens                 | 68.2 ms                                                | 60.7 ms: 1.12x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 96.5 ms: 1.10x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 34.5 ms: 1.10x faster                                                 |
| sympy_integrate         | 13.3 ms                                                | 12.1 ms: 1.10x faster                                                 |
| pylint                  | 307 ms                                                 | 280 ms: 1.10x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 180 ms: 1.09x faster                                                  |
| coroutines              | 20.2 ms                                                | 18.5 ms: 1.09x faster                                                 |
| bench_thread_pool       | 546 us                                                 | 501 us: 1.09x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 49.9 ms: 1.09x faster                                                 |
| 2to3                    | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 67.2 ms: 1.07x faster                                                 |
| unpickle_list           | 2.69 us                                                | 2.50 us: 1.07x faster                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.25 ms: 1.06x faster                                                 |
| json_dumps              | 8.40 ms                                                | 7.91 ms: 1.06x faster                                                 |
| sqlglot_transpile       | 1.57 ms                                                | 1.48 ms: 1.06x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.39 us: 1.06x faster                                                 |
| meteor_contest          | 78.1 ms                                                | 73.8 ms: 1.06x faster                                                 |
| sympy_sum               | 93.6 ms                                                | 88.7 ms: 1.06x faster                                                 |
| mdp                     | 1.66 sec                                               | 1.58 sec: 1.05x faster                                                |
| sympy_expand            | 275 ms                                                 | 262 ms: 1.05x faster                                                  |
| sympy_str               | 169 ms                                                 | 161 ms: 1.05x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.30 ms: 1.05x faster                                                 |
| telco                   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                 |
| json                    | 3.08 ms                                                | 3.04 ms: 1.01x faster                                                 |
| json_loads              | 16.9 us                                                | 16.8 us: 1.01x faster                                                 |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                                 |
| regex_dna               | 162 ms                                                 | 163 ms: 1.01x slower                                                  |
| pickle                  | 7.35 us                                                | 7.42 us: 1.01x slower                                                 |
| flaskblogging           | 2.75 ms                                                | 2.79 ms: 1.01x slower                                                 |
| pickle_list             | 2.80 us                                                | 2.85 us: 1.02x slower                                                 |
| regex_effbot            | 2.46 ms                                                | 2.50 ms: 1.02x slower                                                 |
| regex_v8                | 17.6 ms                                                | 18.0 ms: 1.02x slower                                                 |
| unpickle                | 9.89 us                                                | 10.1 us: 1.02x slower                                                 |
| bench_mp_pool           | 39.7 ms                                                | 42.1 ms: 1.06x slower                                                 |
| python_startup          | 11.9 ms                                                | 12.7 ms: 1.07x slower                                                 |
| coverage                | 42.0 ms                                                | 45.2 ms: 1.07x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (10) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
