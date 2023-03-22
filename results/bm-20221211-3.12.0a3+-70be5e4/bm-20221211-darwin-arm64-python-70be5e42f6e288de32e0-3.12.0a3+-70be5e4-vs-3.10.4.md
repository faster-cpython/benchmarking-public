
# Results vs. 3.10.4

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: darwin-arm64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.25x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 179 ms: 1.12x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.28 ms: 1.36x faster                                                  |
| docutils       | 1.78 sec                                               | 1.44 sec: 1.24x faster                                                 |
| html5lib       | 44.2 ms                                                | 34.3 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 62.8 ms: 1.49x faster                                                  |
| float          | 72.4 ms                                                | 51.9 ms: 1.40x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 72.7 ms: 1.33x faster                                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 196 us: 1.44x faster                                                   |
| json_dumps           | 8.40 ms                                                | 6.17 ms: 1.36x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 152 us: 1.33x faster                                                   |
| xml_etree_process    | 44.8 ms                                                | 34.4 ms: 1.30x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 47.1 ms: 1.15x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 93.1 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 65.6 ms: 1.10x faster                                                  |
| unpickle_list        | 2.69 us                                                | 2.58 us: 1.04x faster                                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                                  |
| unpickle             | 9.89 us                                                | 9.68 us: 1.02x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| pickle_list          | 2.80 us                                                | 2.86 us: 1.02x slower                                                  |
| pickle               | 7.35 us                                                | 7.63 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 9.29 ms: 1.28x faster                                                  |
| python_startup_no_site | 8.88 ms                                                | 7.34 ms: 1.21x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 6.88 ms: 1.52x faster                                                  |
| django_template | 27.3 ms                                                | 20.2 ms: 1.35x faster                                                  |
| genshi_text     | 18.4 ms                                                | 14.0 ms: 1.31x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 28.3 ms: 1.31x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.48 ms: 2.07x faster                                                  |
| logging_silent          | 119 ns                                                 | 62.3 ns: 1.92x faster                                                  |
| richards                | 51.4 ms                                                | 28.9 ms: 1.78x faster                                                  |
| scimark_sor             | 126 ms                                                 | 77.5 ms: 1.63x faster                                                  |
| scimark_lu              | 109 ms                                                 | 69.2 ms: 1.58x faster                                                  |
| go                      | 165 ms                                                 | 106 ms: 1.56x faster                                                   |
| raytrace                | 325 ms                                                 | 211 ms: 1.54x faster                                                   |
| mako                    | 10.5 ms                                                | 6.88 ms: 1.52x faster                                                  |
| scimark_monte_carlo     | 72.5 ms                                                | 48.3 ms: 1.50x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 329 ms: 1.49x faster                                                   |
| nbody                   | 93.3 ms                                                | 62.8 ms: 1.49x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 52.9 ms: 1.48x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 196 us: 1.44x faster                                                   |
| sqlglot_parse           | 1.37 ms                                                | 948 us: 1.44x faster                                                   |
| pathlib                 | 28.8 ms                                                | 20.3 ms: 1.42x faster                                                  |
| sqlglot_transpile       | 1.57 ms                                                | 1.11 ms: 1.42x faster                                                  |
| async_tree_none         | 400 ms                                                 | 285 ms: 1.40x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 726 ms: 1.40x faster                                                   |
| pyflate                 | 453 ms                                                 | 323 ms: 1.40x faster                                                   |
| float                   | 72.4 ms                                                | 51.9 ms: 1.40x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.59 ms: 1.38x faster                                                  |
| pycparser               | 916 ms                                                 | 670 ms: 1.37x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.17 ms: 1.36x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.40 us: 1.36x faster                                                  |
| chaos                   | 66.7 ms                                                | 49.2 ms: 1.36x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.28 ms: 1.36x faster                                                  |
| thrift                  | 580 us                                                 | 429 us: 1.35x faster                                                   |
| django_template         | 27.3 ms                                                | 20.2 ms: 1.35x faster                                                  |
| logging_format          | 4.97 us                                                | 3.71 us: 1.34x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 71.8 ms: 1.34x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 152 us: 1.33x faster                                                   |
| regex_compile           | 96.4 ms                                                | 72.7 ms: 1.33x faster                                                  |
| genshi_text             | 18.4 ms                                                | 14.0 ms: 1.31x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 28.3 ms: 1.31x faster                                                  |
| dulwich_log             | 37.1 ms                                                | 28.4 ms: 1.31x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 34.4 ms: 1.30x faster                                                  |
| html5lib                | 44.2 ms                                                | 34.3 ms: 1.29x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 471 ms: 1.29x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 960 ms: 1.28x faster                                                   |
| python_startup          | 11.9 ms                                                | 9.29 ms: 1.28x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 27.2 us: 1.26x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 30.1 ns: 1.24x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.78 ms: 1.24x faster                                                  |
| fannkuch                | 317 ms                                                 | 256 ms: 1.24x faster                                                   |
| docutils                | 1.78 sec                                               | 1.44 sec: 1.24x faster                                                 |
| async_tree_cpu_io_mixed | 669 ms                                                 | 541 ms: 1.24x faster                                                   |
| bench_thread_pool       | 546 us                                                 | 442 us: 1.24x faster                                                   |
| deepcopy                | 281 us                                                 | 228 us: 1.23x faster                                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.0 ms: 1.23x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.94 us: 1.23x faster                                                  |
| python_startup_no_site  | 8.88 ms                                                | 7.34 ms: 1.21x faster                                                  |
| scimark_fft             | 230 ms                                                 | 194 ms: 1.19x faster                                                   |
| async_generators        | 234 ms                                                 | 198 ms: 1.18x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.3 ms: 1.17x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 168 ms: 1.17x faster                                                   |
| nqueens                 | 68.2 ms                                                | 59.0 ms: 1.16x faster                                                  |
| coroutines              | 20.2 ms                                                | 17.5 ms: 1.15x faster                                                  |
| xml_etree_generate      | 54.2 ms                                                | 47.1 ms: 1.15x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 93.1 ms: 1.14x faster                                                  |
| sympy_expand            | 275 ms                                                 | 241 ms: 1.14x faster                                                   |
| sympy_str               | 169 ms                                                 | 150 ms: 1.13x faster                                                   |
| 2to3                    | 201 ms                                                 | 179 ms: 1.12x faster                                                   |
| mdp                     | 1.66 sec                                               | 1.50 sec: 1.11x faster                                                 |
| xml_etree_iterparse     | 72.3 ms                                                | 65.6 ms: 1.10x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 85.2 ms: 1.10x faster                                                  |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                                  |
| json                    | 3.08 ms                                                | 2.84 ms: 1.09x faster                                                  |
| telco                   | 3.63 ms                                                | 3.35 ms: 1.09x faster                                                  |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| unpickle_list           | 2.69 us                                                | 2.58 us: 1.04x faster                                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 76.3 ms: 1.02x faster                                                  |
| generators              | 32.7 ms                                                | 32.0 ms: 1.02x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.44 us: 1.02x faster                                                  |
| unpickle                | 9.89 us                                                | 9.68 us: 1.02x faster                                                  |
| pidigits                | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.01x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.86 us: 1.02x slower                                                  |
| pickle                  | 7.35 us                                                | 7.63 us: 1.04x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 42.5 ms: 1.07x slower                                                  |
| coverage                | 42.0 ms                                                | 55.2 ms: 1.31x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.25x faster                                                           |
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221211-3.12.0a3+-70be5e4/bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4.json: mypy
