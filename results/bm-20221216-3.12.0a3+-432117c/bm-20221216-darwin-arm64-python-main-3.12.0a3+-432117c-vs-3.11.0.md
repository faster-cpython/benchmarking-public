
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 432117c
- commit date: 2022-12-16
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 184 ms: 1.14x slower                                   |
| chameleon      | 4.57 ms                                                | 4.29 ms: 1.07x faster                                  |
| docutils       | 1.47 sec                                               | 1.44 sec: 1.02x faster                                 |
| html5lib       | 34.7 ms                                                | 33.2 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 62.3 ms: 1.05x faster                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                   |
| float          | 53.0 ms                                                | 53.4 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 72.7 ms: 1.06x faster                                  |
| regex_dna      | 152 ms                                                 | 149 ms: 1.01x faster                                   |
| regex_v8       | 16.2 ms                                                | 16.0 ms: 1.01x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.71 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.16 ms: 1.25x faster                                  |
| xml_etree_parse      | 106 ms                                                 | 92.9 ms: 1.14x faster                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 65.5 ms: 1.06x faster                                  |
| unpickle_pure_python | 159 us                                                 | 151 us: 1.05x faster                                   |
| xml_etree_generate   | 48.8 ms                                                | 47.0 ms: 1.04x faster                                  |
| unpickle_list        | 2.63 us                                                | 2.56 us: 1.03x faster                                  |
| xml_etree_process    | 35.2 ms                                                | 34.4 ms: 1.02x faster                                  |
| pickle_pure_python   | 199 us                                                 | 197 us: 1.01x faster                                   |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pickle_list          | 2.81 us                                                | 2.84 us: 1.01x slower                                  |
| unpickle             | 9.70 us                                                | 9.84 us: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| pickle               | 7.17 us                                                | 7.55 us: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.34 ms: 1.27x faster                                  |
| python_startup         | 11.5 ms                                                | 9.29 ms: 1.24x faster                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.49 ms                                                | 6.96 ms: 1.22x faster                                  |
| genshi_text     | 15.3 ms                                                | 13.9 ms: 1.10x faster                                  |
| genshi_xml      | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| django_template | 21.0 ms                                                | 20.7 ms: 1.02x faster                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.4 ms: 1.36x faster                                  |
| python_startup_no_site  | 9.31 ms                                                | 7.34 ms: 1.27x faster                                  |
| json_dumps              | 7.72 ms                                                | 6.16 ms: 1.25x faster                                  |
| python_startup          | 11.5 ms                                                | 9.29 ms: 1.24x faster                                  |
| mako                    | 8.49 ms                                                | 6.96 ms: 1.22x faster                                  |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.77 ms: 1.16x faster                                  |
| xml_etree_parse         | 106 ms                                                 | 92.9 ms: 1.14x faster                                  |
| deltablue               | 2.81 ms                                                | 2.51 ms: 1.12x faster                                  |
| unpack_sequence         | 33.6 ns                                                | 30.4 ns: 1.11x faster                                  |
| richards                | 32.2 ms                                                | 29.2 ms: 1.10x faster                                  |
| genshi_text             | 15.3 ms                                                | 13.9 ms: 1.10x faster                                  |
| logging_silent          | 68.0 ns                                                | 62.7 ns: 1.08x faster                                  |
| coverage                | 58.6 ms                                                | 54.9 ms: 1.07x faster                                  |
| chameleon               | 4.57 ms                                                | 4.29 ms: 1.07x faster                                  |
| scimark_sor             | 83.0 ms                                                | 78.1 ms: 1.06x faster                                  |
| bench_thread_pool       | 473 us                                                 | 445 us: 1.06x faster                                   |
| xml_etree_iterparse     | 69.2 ms                                                | 65.5 ms: 1.06x faster                                  |
| genshi_xml              | 29.8 ms                                                | 28.2 ms: 1.06x faster                                  |
| regex_compile           | 76.7 ms                                                | 72.7 ms: 1.06x faster                                  |
| dulwich_log             | 29.9 ms                                                | 28.4 ms: 1.05x faster                                  |
| nbody                   | 65.5 ms                                                | 62.3 ms: 1.05x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 151 us: 1.05x faster                                   |
| pycparser               | 697 ms                                                 | 665 ms: 1.05x faster                                   |
| html5lib                | 34.7 ms                                                | 33.2 ms: 1.05x faster                                  |
| scimark_lu              | 72.1 ms                                                | 69.0 ms: 1.05x faster                                  |
| nqueens                 | 61.8 ms                                                | 59.3 ms: 1.04x faster                                  |
| xml_etree_generate      | 48.8 ms                                                | 47.0 ms: 1.04x faster                                  |
| scimark_fft             | 199 ms                                                 | 193 ms: 1.03x faster                                   |
| mdp                     | 1.54 sec                                               | 1.50 sec: 1.03x faster                                 |
| hexiom                  | 4.73 ms                                                | 4.59 ms: 1.03x faster                                  |
| unpickle_list           | 2.63 us                                                | 2.56 us: 1.03x faster                                  |
| go                      | 109 ms                                                 | 106 ms: 1.03x faster                                   |
| xml_etree_process       | 35.2 ms                                                | 34.4 ms: 1.02x faster                                  |
| fannkuch                | 261 ms                                                 | 255 ms: 1.02x faster                                   |
| docutils                | 1.47 sec                                               | 1.44 sec: 1.02x faster                                 |
| sqlglot_normalize       | 171 ms                                                 | 167 ms: 1.02x faster                                   |
| raytrace                | 207 ms                                                 | 203 ms: 1.02x faster                                   |
| logging_simple          | 3.50 us                                                | 3.44 us: 1.02x faster                                  |
| chaos                   | 49.5 ms                                                | 48.6 ms: 1.02x faster                                  |
| django_template         | 21.0 ms                                                | 20.7 ms: 1.02x faster                                  |
| coroutines              | 17.7 ms                                                | 17.4 ms: 1.02x faster                                  |
| spectral_norm           | 72.8 ms                                                | 71.7 ms: 1.01x faster                                  |
| regex_dna               | 152 ms                                                 | 149 ms: 1.01x faster                                   |
| sympy_integrate         | 11.5 ms                                                | 11.3 ms: 1.01x faster                                  |
| telco                   | 3.39 ms                                                | 3.35 ms: 1.01x faster                                  |
| sympy_str               | 152 ms                                                 | 150 ms: 1.01x faster                                   |
| sympy_sum               | 86.0 ms                                                | 85.0 ms: 1.01x faster                                  |
| sqlglot_optimize        | 31.2 ms                                                | 30.8 ms: 1.01x faster                                  |
| regex_v8                | 16.2 ms                                                | 16.0 ms: 1.01x faster                                  |
| sympy_expand            | 243 ms                                                 | 240 ms: 1.01x faster                                   |
| logging_format          | 3.78 us                                                | 3.74 us: 1.01x faster                                  |
| pickle_pure_python      | 199 us                                                 | 197 us: 1.01x faster                                   |
| scimark_monte_carlo     | 46.4 ms                                                | 46.1 ms: 1.01x faster                                  |
| pprint_pformat          | 950 ms                                                 | 955 ms: 1.01x slower                                   |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                   |
| float                   | 53.0 ms                                                | 53.4 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 538 ms: 1.01x slower                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                  |
| pprint_safe_repr        | 465 ms                                                 | 470 ms: 1.01x slower                                   |
| pickle_list             | 2.81 us                                                | 2.84 us: 1.01x slower                                  |
| unpickle                | 9.70 us                                                | 9.84 us: 1.01x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.14 ms: 1.02x slower                                  |
| json_loads              | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| deepcopy                | 224 us                                                 | 227 us: 1.02x slower                                   |
| json                    | 2.77 ms                                                | 2.82 ms: 1.02x slower                                  |
| sqlglot_parse           | 957 us                                                 | 976 us: 1.02x slower                                   |
| deepcopy_reduce         | 1.91 us                                                | 1.95 us: 1.02x slower                                  |
| meteor_contest          | 73.8 ms                                                | 75.4 ms: 1.02x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 53.0 ms: 1.02x slower                                  |
| async_generators        | 195 ms                                                 | 201 ms: 1.03x slower                                   |
| regex_effbot            | 2.63 ms                                                | 2.71 ms: 1.03x slower                                  |
| async_tree_io           | 706 ms                                                 | 732 ms: 1.04x slower                                   |
| deepcopy_memo           | 26.3 us                                                | 27.4 us: 1.04x slower                                  |
| pyflate                 | 311 ms                                                 | 324 ms: 1.04x slower                                   |
| pickle                  | 7.17 us                                                | 7.55 us: 1.05x slower                                  |
| generators              | 28.8 ms                                                | 32.2 ms: 1.12x slower                                  |
| sqlite_synth            | 1.27 us                                                | 1.43 us: 1.13x slower                                  |
| 2to3                    | 161 ms                                                 | 184 ms: 1.14x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (4): async_tree_memoization, thrift, async_tree_none, bench_mp_pool
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221216-3.12.0a3+-432117c/bm-20221216-darwin-arm64-python-main-3.12.0a3+-432117c.json: mypy
