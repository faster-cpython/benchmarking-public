
# Results vs. 3.11.0

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: darwin-arm64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 179 ms: 1.11x slower                                                   |
| chameleon      | 4.57 ms                                                | 4.28 ms: 1.07x faster                                                  |
| docutils       | 1.47 sec                                               | 1.44 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 62.8 ms: 1.04x faster                                                  |
| float          | 53.0 ms                                                | 51.9 ms: 1.02x faster                                                  |
| pidigits       | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 72.7 ms: 1.05x faster                                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| regex_effbot   | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.17 ms: 1.25x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 93.1 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 65.6 ms: 1.06x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 152 us: 1.04x faster                                                   |
| xml_etree_generate   | 48.8 ms                                                | 47.1 ms: 1.04x faster                                                  |
| xml_etree_process    | 35.2 ms                                                | 34.4 ms: 1.02x faster                                                  |
| unpickle_list        | 2.63 us                                                | 2.58 us: 1.02x faster                                                  |
| pickle_pure_python   | 199 us                                                 | 196 us: 1.01x faster                                                   |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.02x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                                  |
| pickle               | 7.17 us                                                | 7.63 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.34 ms: 1.27x faster                                                  |
| python_startup         | 11.5 ms                                                | 9.29 ms: 1.24x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 6.88 ms: 1.23x faster                                                  |
| genshi_text     | 15.3 ms                                                | 14.0 ms: 1.09x faster                                                  |
| genshi_xml      | 29.8 ms                                                | 28.3 ms: 1.05x faster                                                  |
| django_template | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.3 ms: 1.37x faster                                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.34 ms: 1.27x faster                                                  |
| json_dumps              | 7.72 ms                                                | 6.17 ms: 1.25x faster                                                  |
| python_startup          | 11.5 ms                                                | 9.29 ms: 1.24x faster                                                  |
| mako                    | 8.49 ms                                                | 6.88 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.78 ms: 1.15x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 93.1 ms: 1.14x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.48 ms: 1.13x faster                                                  |
| unpack_sequence         | 33.6 ns                                                | 30.1 ns: 1.11x faster                                                  |
| richards                | 32.2 ms                                                | 28.9 ms: 1.11x faster                                                  |
| logging_silent          | 68.0 ns                                                | 62.3 ns: 1.09x faster                                                  |
| genshi_text             | 15.3 ms                                                | 14.0 ms: 1.09x faster                                                  |
| scimark_sor             | 83.0 ms                                                | 77.5 ms: 1.07x faster                                                  |
| chameleon               | 4.57 ms                                                | 4.28 ms: 1.07x faster                                                  |
| bench_thread_pool       | 473 us                                                 | 442 us: 1.07x faster                                                   |
| coverage                | 58.6 ms                                                | 55.2 ms: 1.06x faster                                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 65.6 ms: 1.06x faster                                                  |
| regex_compile           | 76.7 ms                                                | 72.7 ms: 1.05x faster                                                  |
| dulwich_log             | 29.9 ms                                                | 28.4 ms: 1.05x faster                                                  |
| genshi_xml              | 29.8 ms                                                | 28.3 ms: 1.05x faster                                                  |
| nqueens                 | 61.8 ms                                                | 59.0 ms: 1.05x faster                                                  |
| nbody                   | 65.5 ms                                                | 62.8 ms: 1.04x faster                                                  |
| scimark_lu              | 72.1 ms                                                | 69.2 ms: 1.04x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 152 us: 1.04x faster                                                   |
| django_template         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                  |
| pycparser               | 697 ms                                                 | 670 ms: 1.04x faster                                                   |
| xml_etree_generate      | 48.8 ms                                                | 47.1 ms: 1.04x faster                                                  |
| mdp                     | 1.54 sec                                               | 1.50 sec: 1.03x faster                                                 |
| hexiom                  | 4.73 ms                                                | 4.59 ms: 1.03x faster                                                  |
| logging_simple          | 3.50 us                                                | 3.40 us: 1.03x faster                                                  |
| scimark_fft             | 199 ms                                                 | 194 ms: 1.03x faster                                                   |
| xml_etree_process       | 35.2 ms                                                | 34.4 ms: 1.02x faster                                                  |
| go                      | 109 ms                                                 | 106 ms: 1.02x faster                                                   |
| docutils                | 1.47 sec                                               | 1.44 sec: 1.02x faster                                                 |
| float                   | 53.0 ms                                                | 51.9 ms: 1.02x faster                                                  |
| unpickle_list           | 2.63 us                                                | 2.58 us: 1.02x faster                                                  |
| sqlglot_normalize       | 171 ms                                                 | 168 ms: 1.02x faster                                                   |
| fannkuch                | 261 ms                                                 | 256 ms: 1.02x faster                                                   |
| logging_format          | 3.78 us                                                | 3.71 us: 1.02x faster                                                  |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                                   |
| telco                   | 3.39 ms                                                | 3.35 ms: 1.01x faster                                                  |
| spectral_norm           | 72.8 ms                                                | 71.8 ms: 1.01x faster                                                  |
| pickle_pure_python      | 199 us                                                 | 196 us: 1.01x faster                                                   |
| sympy_integrate         | 11.5 ms                                                | 11.3 ms: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                | 2.60 ms: 1.01x faster                                                  |
| coroutines              | 17.7 ms                                                | 17.5 ms: 1.01x faster                                                  |
| sqlglot_parse           | 957 us                                                 | 948 us: 1.01x faster                                                   |
| thrift                  | 433 us                                                 | 429 us: 1.01x faster                                                   |
| sympy_sum               | 86.0 ms                                                | 85.2 ms: 1.01x faster                                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.11 ms: 1.01x faster                                                  |
| sympy_str               | 152 ms                                                 | 150 ms: 1.01x faster                                                   |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                  |
| sympy_expand            | 243 ms                                                 | 241 ms: 1.01x faster                                                   |
| sqlglot_optimize        | 31.2 ms                                                | 31.0 ms: 1.01x faster                                                  |
| chaos                   | 49.5 ms                                                | 49.2 ms: 1.01x faster                                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| pidigits                | 281 ms                                                 | 283 ms: 1.01x slower                                                   |
| pprint_pformat          | 950 ms                                                 | 960 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 534 ms                                                 | 541 ms: 1.01x slower                                                   |
| deepcopy_reduce         | 1.91 us                                                | 1.94 us: 1.01x slower                                                  |
| pprint_safe_repr        | 465 ms                                                 | 471 ms: 1.01x slower                                                   |
| json_loads              | 16.1 us                                                | 16.3 us: 1.02x slower                                                  |
| async_generators        | 195 ms                                                 | 198 ms: 1.02x slower                                                   |
| raytrace                | 207 ms                                                 | 211 ms: 1.02x slower                                                   |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                                  |
| deepcopy                | 224 us                                                 | 228 us: 1.02x slower                                                   |
| crypto_pyaes            | 51.7 ms                                                | 52.9 ms: 1.02x slower                                                  |
| json                    | 2.77 ms                                                | 2.84 ms: 1.02x slower                                                  |
| async_tree_io           | 706 ms                                                 | 726 ms: 1.03x slower                                                   |
| meteor_contest          | 73.8 ms                                                | 76.3 ms: 1.03x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 27.2 us: 1.04x slower                                                  |
| pyflate                 | 311 ms                                                 | 323 ms: 1.04x slower                                                   |
| scimark_monte_carlo     | 46.4 ms                                                | 48.3 ms: 1.04x slower                                                  |
| pickle                  | 7.17 us                                                | 7.63 us: 1.07x slower                                                  |
| generators              | 28.8 ms                                                | 32.0 ms: 1.11x slower                                                  |
| 2to3                    | 161 ms                                                 | 179 ms: 1.11x slower                                                   |
| sqlite_synth            | 1.27 us                                                | 1.44 us: 1.13x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (5): async_tree_memoization, bench_mp_pool, html5lib, unpickle, async_tree_none
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221211-3.12.0a3+-70be5e4/bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4.json: mypy
