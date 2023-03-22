
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 432117c
- commit date: 2022-12-16
- overall geometric mean: 1.25x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 184 ms: 1.09x faster                                   |
| chameleon      | 5.79 ms                                                | 4.29 ms: 1.35x faster                                  |
| docutils       | 1.78 sec                                               | 1.44 sec: 1.24x faster                                 |
| html5lib       | 44.2 ms                                                | 33.2 ms: 1.33x faster                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 62.3 ms: 1.50x faster                                  |
| float          | 72.4 ms                                                | 53.4 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 72.7 ms: 1.33x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.0 ms: 1.10x faster                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.71 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 197 us: 1.43x faster                                   |
| json_dumps           | 8.40 ms                                                | 6.16 ms: 1.36x faster                                  |
| unpickle_pure_python | 203 us                                                 | 151 us: 1.34x faster                                   |
| xml_etree_process    | 44.8 ms                                                | 34.4 ms: 1.30x faster                                  |
| xml_etree_generate   | 54.2 ms                                                | 47.0 ms: 1.15x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 92.9 ms: 1.15x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 65.5 ms: 1.10x faster                                  |
| unpickle_list        | 2.69 us                                                | 2.56 us: 1.05x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle_list          | 2.80 us                                                | 2.84 us: 1.01x slower                                  |
| pickle               | 7.35 us                                                | 7.55 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.29 ms: 1.28x faster                                  |
| python_startup_no_site | 8.88 ms                                                | 7.34 ms: 1.21x faster                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 6.96 ms: 1.51x faster                                  |
| genshi_text     | 18.4 ms                                                | 13.9 ms: 1.32x faster                                  |
| django_template | 27.3 ms                                                | 20.7 ms: 1.32x faster                                  |
| genshi_xml      | 37.2 ms                                                | 28.2 ms: 1.32x faster                                  |
| Geometric mean  | (ref)                                                  | 1.36x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.51 ms: 2.05x faster                                  |
| logging_silent          | 119 ns                                                 | 62.7 ns: 1.91x faster                                  |
| richards                | 51.4 ms                                                | 29.2 ms: 1.76x faster                                  |
| scimark_sor             | 126 ms                                                 | 78.1 ms: 1.61x faster                                  |
| raytrace                | 325 ms                                                 | 203 ms: 1.60x faster                                   |
| scimark_lu              | 109 ms                                                 | 69.0 ms: 1.58x faster                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 46.1 ms: 1.57x faster                                  |
| go                      | 165 ms                                                 | 106 ms: 1.56x faster                                   |
| mako                    | 10.5 ms                                                | 6.96 ms: 1.51x faster                                  |
| nbody                   | 93.3 ms                                                | 62.3 ms: 1.50x faster                                  |
| async_tree_memoization  | 490 ms                                                 | 330 ms: 1.48x faster                                   |
| crypto_pyaes            | 78.1 ms                                                | 53.0 ms: 1.47x faster                                  |
| pickle_pure_python      | 283 us                                                 | 197 us: 1.43x faster                                   |
| pathlib                 | 28.8 ms                                                | 20.4 ms: 1.41x faster                                  |
| async_tree_none         | 400 ms                                                 | 285 ms: 1.40x faster                                   |
| sqlglot_parse           | 1.37 ms                                                | 976 us: 1.40x faster                                   |
| pyflate                 | 453 ms                                                 | 324 ms: 1.40x faster                                   |
| async_tree_io           | 1.02 sec                                               | 732 ms: 1.39x faster                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.14 ms: 1.38x faster                                  |
| pycparser               | 916 ms                                                 | 665 ms: 1.38x faster                                   |
| hexiom                  | 6.32 ms                                                | 4.59 ms: 1.38x faster                                  |
| chaos                   | 66.7 ms                                                | 48.6 ms: 1.37x faster                                  |
| json_dumps              | 8.40 ms                                                | 6.16 ms: 1.36x faster                                  |
| float                   | 72.4 ms                                                | 53.4 ms: 1.36x faster                                  |
| chameleon               | 5.79 ms                                                | 4.29 ms: 1.35x faster                                  |
| logging_simple          | 4.63 us                                                | 3.44 us: 1.35x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 151 us: 1.34x faster                                   |
| thrift                  | 580 us                                                 | 433 us: 1.34x faster                                   |
| spectral_norm           | 95.8 ms                                                | 71.7 ms: 1.34x faster                                  |
| html5lib                | 44.2 ms                                                | 33.2 ms: 1.33x faster                                  |
| logging_format          | 4.97 us                                                | 3.74 us: 1.33x faster                                  |
| regex_compile           | 96.4 ms                                                | 72.7 ms: 1.33x faster                                  |
| genshi_text             | 18.4 ms                                                | 13.9 ms: 1.32x faster                                  |
| django_template         | 27.3 ms                                                | 20.7 ms: 1.32x faster                                  |
| genshi_xml              | 37.2 ms                                                | 28.2 ms: 1.32x faster                                  |
| dulwich_log             | 37.1 ms                                                | 28.4 ms: 1.31x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 34.4 ms: 1.30x faster                                  |
| pprint_pformat          | 1.23 sec                                               | 955 ms: 1.29x faster                                   |
| pprint_safe_repr        | 606 ms                                                 | 470 ms: 1.29x faster                                   |
| python_startup          | 11.9 ms                                                | 9.29 ms: 1.28x faster                                  |
| deepcopy_memo           | 34.4 us                                                | 27.4 us: 1.26x faster                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.77 ms: 1.25x faster                                  |
| fannkuch                | 317 ms                                                 | 255 ms: 1.25x faster                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 538 ms: 1.24x faster                                   |
| docutils                | 1.78 sec                                               | 1.44 sec: 1.24x faster                                 |
| deepcopy                | 281 us                                                 | 227 us: 1.24x faster                                   |
| sqlglot_optimize        | 38.0 ms                                                | 30.8 ms: 1.23x faster                                  |
| unpack_sequence         | 37.4 ns                                                | 30.4 ns: 1.23x faster                                  |
| bench_thread_pool       | 546 us                                                 | 445 us: 1.23x faster                                   |
| deepcopy_reduce         | 2.37 us                                                | 1.95 us: 1.22x faster                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.34 ms: 1.21x faster                                  |
| scimark_fft             | 230 ms                                                 | 193 ms: 1.19x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.3 ms: 1.17x faster                                  |
| sqlglot_normalize       | 196 ms                                                 | 167 ms: 1.17x faster                                   |
| async_generators        | 234 ms                                                 | 201 ms: 1.17x faster                                   |
| coroutines              | 20.2 ms                                                | 17.4 ms: 1.16x faster                                  |
| xml_etree_generate      | 54.2 ms                                                | 47.0 ms: 1.15x faster                                  |
| nqueens                 | 68.2 ms                                                | 59.3 ms: 1.15x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 92.9 ms: 1.15x faster                                  |
| sympy_expand            | 275 ms                                                 | 240 ms: 1.15x faster                                   |
| sympy_str               | 169 ms                                                 | 150 ms: 1.13x faster                                   |
| mdp                     | 1.66 sec                                               | 1.50 sec: 1.11x faster                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 65.5 ms: 1.10x faster                                  |
| sympy_sum               | 93.6 ms                                                | 85.0 ms: 1.10x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.0 ms: 1.10x faster                                  |
| json                    | 3.08 ms                                                | 2.82 ms: 1.09x faster                                  |
| 2to3                    | 201 ms                                                 | 184 ms: 1.09x faster                                   |
| telco                   | 3.63 ms                                                | 3.35 ms: 1.08x faster                                  |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                   |
| unpickle_list           | 2.69 us                                                | 2.56 us: 1.05x faster                                  |
| meteor_contest          | 78.1 ms                                                | 75.4 ms: 1.04x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.43 us: 1.03x faster                                  |
| generators              | 32.7 ms                                                | 32.2 ms: 1.02x faster                                  |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle_list             | 2.80 us                                                | 2.84 us: 1.01x slower                                  |
| pickle                  | 7.35 us                                                | 7.55 us: 1.03x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.71 ms: 1.10x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 43.9 ms: 1.11x slower                                  |
| coverage                | 42.0 ms                                                | 54.9 ms: 1.31x slower                                  |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (2): unpickle, pidigits
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221216-3.12.0a3+-432117c/bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c.json: mypy
