
# Results vs. 3.11.0

- fork: python
- ref: 5b3a2569f4b4dfb58a8f
- machine: darwin-arm64
- commit hash: 5b3a256
- commit date: 2022-09-19
- overall geometric mean: 1.01x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.69 ms: 1.03x slower                                                 |
| docutils       | 1.47 sec                                               | 1.48 sec: 1.00x slower                                                |
| html5lib       | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| float          | 53.0 ms                                                | 55.9 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.67 ms: 1.02x slower                                                 |
| regex_dna      | 152 ms                                                 | 155 ms: 1.02x slower                                                  |
| regex_v8       | 16.2 ms                                                | 16.7 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.72 ms                                                | 6.09 ms: 1.27x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                | 64.8 ms: 1.07x faster                                                 |
| unpickle_list        | 2.63 us                                                | 2.54 us: 1.04x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 47.5 ms: 1.03x faster                                                 |
| xml_etree_process    | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                 |
| json_loads           | 16.1 us                                                | 16.1 us: 1.00x slower                                                 |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 161 us: 1.01x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 206 us: 1.04x slower                                                  |
| pickle               | 7.17 us                                                | 7.52 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.31 ms                                                | 7.30 ms: 1.28x faster                                                 |
| python_startup         | 11.5 ms                                                | 9.22 ms: 1.25x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.49 ms                                                | 8.14 ms: 1.04x faster                                                 |
| genshi_xml      | 29.8 ms                                                | 30.1 ms: 1.01x slower                                                 |
| django_template | 21.0 ms                                                | 21.8 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pathlib                 | 27.8 ms                                                | 20.6 ms: 1.35x faster                                                 |
| python_startup_no_site  | 9.31 ms                                                | 7.30 ms: 1.28x faster                                                 |
| json_dumps              | 7.72 ms                                                | 6.09 ms: 1.27x faster                                                 |
| python_startup          | 11.5 ms                                                | 9.22 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult | 3.20 ms                                                | 2.83 ms: 1.13x faster                                                 |
| xml_etree_parse         | 106 ms                                                 | 96.1 ms: 1.11x faster                                                 |
| coverage                | 58.6 ms                                                | 53.3 ms: 1.10x faster                                                 |
| flaskblogging           | 2.42 ms                                                | 2.24 ms: 1.08x faster                                                 |
| xml_etree_iterparse     | 69.2 ms                                                | 64.8 ms: 1.07x faster                                                 |
| bench_mp_pool           | 43.2 ms                                                | 41.4 ms: 1.04x faster                                                 |
| mako                    | 8.49 ms                                                | 8.14 ms: 1.04x faster                                                 |
| bench_thread_pool       | 473 us                                                 | 455 us: 1.04x faster                                                  |
| unpickle_list           | 2.63 us                                                | 2.54 us: 1.04x faster                                                 |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.07 ms: 1.03x faster                                                 |
| xml_etree_generate      | 48.8 ms                                                | 47.5 ms: 1.03x faster                                                 |
| dulwich_log             | 29.9 ms                                                | 29.1 ms: 1.02x faster                                                 |
| pylint                  | 271 ms                                                 | 264 ms: 1.02x faster                                                  |
| sqlalchemy_declarative  | 62.7 ms                                                | 61.3 ms: 1.02x faster                                                 |
| logging_silent          | 68.0 ns                                                | 66.5 ns: 1.02x faster                                                 |
| regex_compile           | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                 |
| telco                   | 3.39 ms                                                | 3.36 ms: 1.01x faster                                                 |
| mdp                     | 1.54 sec                                               | 1.53 sec: 1.01x faster                                                |
| async_tree_cpu_io_mixed | 534 ms                                                 | 529 ms: 1.01x faster                                                  |
| async_tree_none         | 285 ms                                                 | 282 ms: 1.01x faster                                                  |
| xml_etree_process       | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                 |
| scimark_fft             | 199 ms                                                 | 199 ms: 1.00x faster                                                  |
| json_loads              | 16.1 us                                                | 16.1 us: 1.00x slower                                                 |
| docutils                | 1.47 sec                                               | 1.48 sec: 1.00x slower                                                |
| crypto_pyaes            | 51.7 ms                                                | 52.0 ms: 1.00x slower                                                 |
| scimark_lu              | 72.1 ms                                                | 72.4 ms: 1.01x slower                                                 |
| pidigits                | 281 ms                                                 | 282 ms: 1.01x slower                                                  |
| deltablue               | 2.81 ms                                                | 2.83 ms: 1.01x slower                                                 |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.1 ms: 1.01x slower                                                 |
| generators              | 28.8 ms                                                | 29.2 ms: 1.01x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 161 us: 1.01x slower                                                  |
| regex_effbot            | 2.63 ms                                                | 2.67 ms: 1.02x slower                                                 |
| sympy_str               | 152 ms                                                 | 154 ms: 1.02x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.02x slower                                                 |
| unpack_sequence         | 33.6 ns                                                | 34.2 ns: 1.02x slower                                                 |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                                  |
| thrift                  | 433 us                                                 | 443 us: 1.02x slower                                                  |
| sympy_expand            | 243 ms                                                 | 248 ms: 1.02x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.9 ms: 1.02x slower                                                 |
| json                    | 2.77 ms                                                | 2.84 ms: 1.02x slower                                                 |
| regex_dna               | 152 ms                                                 | 155 ms: 1.02x slower                                                  |
| pycparser               | 697 ms                                                 | 713 ms: 1.02x slower                                                  |
| chaos                   | 49.5 ms                                                | 50.7 ms: 1.02x slower                                                 |
| chameleon               | 4.57 ms                                                | 4.69 ms: 1.03x slower                                                 |
| async_generators        | 195 ms                                                 | 201 ms: 1.03x slower                                                  |
| html5lib                | 34.7 ms                                                | 35.8 ms: 1.03x slower                                                 |
| regex_v8                | 16.2 ms                                                | 16.7 ms: 1.03x slower                                                 |
| richards                | 32.2 ms                                                | 33.3 ms: 1.03x slower                                                 |
| async_tree_io           | 706 ms                                                 | 732 ms: 1.04x slower                                                  |
| raytrace                | 207 ms                                                 | 215 ms: 1.04x slower                                                  |
| pickle_pure_python      | 199 us                                                 | 206 us: 1.04x slower                                                  |
| django_template         | 21.0 ms                                                | 21.8 ms: 1.04x slower                                                 |
| hexiom                  | 4.73 ms                                                | 4.92 ms: 1.04x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.17 ms: 1.04x slower                                                 |
| fannkuch                | 261 ms                                                 | 272 ms: 1.04x slower                                                  |
| logging_simple          | 3.50 us                                                | 3.65 us: 1.04x slower                                                 |
| logging_format          | 3.78 us                                                | 3.94 us: 1.04x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.00 ms: 1.05x slower                                                 |
| pickle                  | 7.17 us                                                | 7.52 us: 1.05x slower                                                 |
| float                   | 53.0 ms                                                | 55.9 ms: 1.06x slower                                                 |
| meteor_contest          | 73.8 ms                                                | 77.9 ms: 1.06x slower                                                 |
| pprint_pformat          | 950 ms                                                 | 1.01 sec: 1.06x slower                                                |
| pprint_safe_repr        | 465 ms                                                 | 496 ms: 1.07x slower                                                  |
| deepcopy                | 224 us                                                 | 240 us: 1.07x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.07 us: 1.08x slower                                                 |
| go                      | 109 ms                                                 | 118 ms: 1.09x slower                                                  |
| deepcopy_memo           | 26.3 us                                                | 28.7 us: 1.09x slower                                                 |
| coroutines              | 17.7 ms                                                | 19.5 ms: 1.10x slower                                                 |
| pyflate                 | 311 ms                                                 | 350 ms: 1.13x slower                                                  |
| async_tree_memoization  | 336 ms                                                 | 381 ms: 1.14x slower                                                  |
| sqlite_synth            | 1.27 us                                                | 1.45 us: 1.14x slower                                                 |
| 2to3                    | 161 ms                                                 | 185 ms: 1.15x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 54.4 ms: 1.17x slower                                                 |
| scimark_sor             | 83.0 ms                                                | 101 ms: 1.22x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (8): tornado_http, nqueens, unpickle, nbody, pickle_dict, sympy_sum, spectral_norm, genshi_text
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, gc_traversal, gunicorn, mypy2
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220919-3.12.0a0-5b3a256/bm-20220919-darwin-arm64-python-5b3a2569f4b4dfb58a8f-3.12.0a0-5b3a256.json: mypy
