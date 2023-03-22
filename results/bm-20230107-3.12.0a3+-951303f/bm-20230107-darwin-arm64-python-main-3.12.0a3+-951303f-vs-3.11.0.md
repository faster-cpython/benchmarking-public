
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 951303f
- commit date: 2023-01-07
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 182 ms: 1.13x slower                                   |
| chameleon      | 4.57 ms                                                | 4.48 ms: 1.02x faster                                  |
| docutils       | 1.47 sec                                               | 1.43 sec: 1.03x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.6 ms: 1.03x faster                                  |
| nbody          | 65.5 ms                                                | 63.8 ms: 1.03x faster                                  |
| pidigits       | 281 ms                                                 | 277 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.2 ms: 1.02x faster                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| regex_effbot   | 2.63 ms                                                | 2.61 ms: 1.01x faster                                  |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.10 ms: 1.27x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 92.8 ms: 1.14x faster                                  |
| unpickle_pure_python | 159 us                                                 | 142 us: 1.12x faster                                   |
| unpickle             | 9.70 us                                                | 9.05 us: 1.07x faster                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 66.2 ms: 1.05x faster                                  |
| pickle_pure_python   | 199 us                                                 | 192 us: 1.03x faster                                   |
| xml_etree_process    | 35.2 ms                                                | 34.7 ms: 1.01x faster                                  |
| xml_etree_generate   | 48.8 ms                                                | 48.5 ms: 1.01x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| pickle_list          | 2.81 us                                                | 2.86 us: 1.02x slower                                  |
| pickle               | 7.17 us                                                | 7.52 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.32 ms: 1.27x faster                                  |
| python_startup         | 11.5 ms                                                | 9.28 ms: 1.24x faster                                  |
| Geometric mean         | (ref)                                                  | 1.26x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.49 ms                                                | 7.10 ms: 1.20x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| genshi_xml      | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| django_template | 21.0 ms                                                | 21.3 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.8 ms: 1.34x faster                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.32 ms: 1.27x faster                                  |
| json_dumps              | 7.72 ms                                                | 6.10 ms: 1.27x faster                                  |
| python_startup          | 11.5 ms                                                | 9.28 ms: 1.24x faster                                  |
| mako                    | 8.49 ms                                                | 7.10 ms: 1.20x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 92.8 ms: 1.14x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.82 ms: 1.13x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 142 us: 1.12x faster                                   |
| deltablue               | 2.81 ms                                                | 2.56 ms: 1.10x faster                                  |
| unpickle                | 9.70 us                                                | 9.05 us: 1.07x faster                                  |
| genshi_text             | 15.3 ms                                                | 14.3 ms: 1.07x faster                                  |
| richards                | 32.2 ms                                                | 30.4 ms: 1.06x faster                                  |
| genshi_xml              | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| bench_thread_pool       | 473 us                                                 | 450 us: 1.05x faster                                   |
| logging_silent          | 68.0 ns                                                | 64.9 ns: 1.05x faster                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 66.2 ms: 1.05x faster                                  |
| dulwich_log             | 29.9 ms                                                | 28.7 ms: 1.04x faster                                  |
| pickle_pure_python      | 199 us                                                 | 192 us: 1.03x faster                                   |
| unpack_sequence         | 33.6 ns                                                | 32.5 ns: 1.03x faster                                  |
| bench_mp_pool           | 43.2 ms                                                | 41.9 ms: 1.03x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 25.6 us: 1.03x faster                                  |
| pprint_pformat          | 950 ms                                                 | 925 ms: 1.03x faster                                   |
| nqueens                 | 61.8 ms                                                | 60.2 ms: 1.03x faster                                  |
| float                   | 53.0 ms                                                | 51.6 ms: 1.03x faster                                  |
| docutils                | 1.47 sec                                               | 1.43 sec: 1.03x faster                                 |
| nbody                   | 65.5 ms                                                | 63.8 ms: 1.03x faster                                  |
| deepcopy                | 224 us                                                 | 219 us: 1.02x faster                                   |
| async_tree_memoization  | 336 ms                                                 | 328 ms: 1.02x faster                                   |
| coverage                | 58.6 ms                                                | 57.3 ms: 1.02x faster                                  |
| chameleon               | 4.57 ms                                                | 4.48 ms: 1.02x faster                                  |
| regex_compile           | 76.7 ms                                                | 75.2 ms: 1.02x faster                                  |
| pprint_safe_repr        | 465 ms                                                 | 455 ms: 1.02x faster                                   |
| scimark_fft             | 199 ms                                                 | 195 ms: 1.02x faster                                   |
| pycparser               | 697 ms                                                 | 685 ms: 1.02x faster                                   |
| regex_dna               | 152 ms                                                 | 149 ms: 1.02x faster                                   |
| xml_etree_process       | 35.2 ms                                                | 34.7 ms: 1.01x faster                                  |
| pidigits                | 281 ms                                                 | 277 ms: 1.01x faster                                   |
| go                      | 109 ms                                                 | 108 ms: 1.01x faster                                   |
| fannkuch                | 261 ms                                                 | 258 ms: 1.01x faster                                   |
| regex_effbot            | 2.63 ms                                                | 2.61 ms: 1.01x faster                                  |
| sympy_expand            | 243 ms                                                 | 241 ms: 1.01x faster                                   |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                  |
| scimark_sor             | 83.0 ms                                                | 82.4 ms: 1.01x faster                                  |
| sympy_integrate         | 11.5 ms                                                | 11.4 ms: 1.01x faster                                  |
| xml_etree_generate      | 48.8 ms                                                | 48.5 ms: 1.01x faster                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.0 ms: 1.01x faster                                  |
| sqlglot_normalize       | 171 ms                                                 | 170 ms: 1.01x faster                                   |
| mdp                     | 1.54 sec                                               | 1.53 sec: 1.01x faster                                 |
| scimark_lu              | 72.1 ms                                                | 71.9 ms: 1.00x faster                                  |
| logging_simple          | 3.50 us                                                | 3.52 us: 1.00x slower                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| async_tree_none         | 285 ms                                                 | 287 ms: 1.01x slower                                   |
| logging_format          | 3.78 us                                                | 3.81 us: 1.01x slower                                  |
| hexiom                  | 4.73 ms                                                | 4.78 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 541 ms: 1.01x slower                                   |
| thrift                  | 433 us                                                 | 439 us: 1.01x slower                                   |
| django_template         | 21.0 ms                                                | 21.3 ms: 1.01x slower                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.01x slower                                  |
| chaos                   | 49.5 ms                                                | 50.3 ms: 1.02x slower                                  |
| pickle_list             | 2.81 us                                                | 2.86 us: 1.02x slower                                  |
| telco                   | 3.39 ms                                                | 3.47 ms: 1.02x slower                                  |
| json                    | 2.77 ms                                                | 2.84 ms: 1.02x slower                                  |
| async_generators        | 195 ms                                                 | 200 ms: 1.03x slower                                   |
| meteor_contest          | 73.8 ms                                                | 76.3 ms: 1.03x slower                                  |
| pyflate                 | 311 ms                                                 | 322 ms: 1.04x slower                                   |
| crypto_pyaes            | 51.7 ms                                                | 53.7 ms: 1.04x slower                                  |
| async_tree_io           | 706 ms                                                 | 736 ms: 1.04x slower                                   |
| pickle                  | 7.17 us                                                | 7.52 us: 1.05x slower                                  |
| coroutines              | 17.7 ms                                                | 18.8 ms: 1.06x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.35 us: 1.06x slower                                  |
| raytrace                | 207 ms                                                 | 221 ms: 1.07x slower                                   |
| sqlglot_transpile       | 1.12 ms                                                | 1.20 ms: 1.07x slower                                  |
| sqlglot_parse           | 957 us                                                 | 1.04 ms: 1.08x slower                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 51.0 ms: 1.10x slower                                  |
| 2to3                    | 161 ms                                                 | 182 ms: 1.13x slower                                   |
| generators              | 28.8 ms                                                | 33.7 ms: 1.17x slower                                  |
| Geometric mean          | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (6): deepcopy_reduce, sympy_sum, sympy_str, spectral_norm, unpickle_list, html5lib
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230107-3.12.0a3+-951303f/bm-20230107-darwin-arm64-python-main-3.12.0a3+-951303f.json: mypy
