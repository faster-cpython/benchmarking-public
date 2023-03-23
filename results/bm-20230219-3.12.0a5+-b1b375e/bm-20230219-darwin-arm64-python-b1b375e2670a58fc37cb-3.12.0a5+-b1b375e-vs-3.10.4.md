
# Results vs. 3.10.4

- fork: python
- ref: b1b375e2670a58fc37cb
- machine: darwin-arm64
- commit hash: b1b375e
- commit date: 2023-02-19
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 162 ms: 1.24x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.44 ms: 1.31x faster                                                  |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.19x faster                                                 |
| html5lib       | 44.2 ms                                                | 35.8 ms: 1.24x faster                                                  |
| tornado_http   | 91.5 ms                                                | 70.3 ms: 1.30x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.1 ms: 1.46x faster                                                  |
| float          | 72.4 ms                                                | 52.4 ms: 1.38x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 73.0 ms: 1.32x faster                                                  |
| regex_v8       | 17.6 ms                                                | 15.8 ms: 1.11x faster                                                  |
| regex_dna      | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 195 us: 1.46x faster                                                   |
| unpickle_pure_python | 203 us                                                 | 143 us: 1.43x faster                                                   |
| json_dumps           | 8.40 ms                                                | 6.15 ms: 1.37x faster                                                  |
| xml_etree_process    | 44.8 ms                                                | 36.0 ms: 1.24x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 97.6 ms: 1.09x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 50.3 ms: 1.08x faster                                                  |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| unpickle_list        | 2.69 us                                                | 2.57 us: 1.05x faster                                                  |
| unpickle             | 9.89 us                                                | 9.65 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 70.9 ms: 1.02x faster                                                  |
| pickle_dict          | 17.9 us                                                | 18.1 us: 1.01x slower                                                  |
| pickle_list          | 2.80 us                                                | 2.84 us: 1.01x slower                                                  |
| pickle               | 7.35 us                                                | 7.56 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.4 ms: 1.04x slower                                                  |
| python_startup_no_site | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.36 ms: 1.42x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 28.3 ms: 1.31x faster                                                  |
| genshi_text     | 18.4 ms                                                | 14.3 ms: 1.28x faster                                                  |
| django_template | 27.3 ms                                                | 21.3 ms: 1.28x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230219-darwin-arm64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.57 ms: 2.00x faster                                                  |
| logging_silent          | 119 ns                                                 | 65.8 ns: 1.81x faster                                                  |
| richards                | 51.4 ms                                                | 30.0 ms: 1.71x faster                                                  |
| go                      | 165 ms                                                 | 109 ms: 1.52x faster                                                   |
| asyncio_tcp             | 670 ms                                                 | 441 ms: 1.52x faster                                                   |
| scimark_lu              | 109 ms                                                 | 73.3 ms: 1.49x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 329 ms: 1.49x faster                                                   |
| hexiom                  | 6.32 ms                                                | 4.31 ms: 1.47x faster                                                  |
| crypto_pyaes            | 78.1 ms                                                | 53.5 ms: 1.46x faster                                                  |
| raytrace                | 325 ms                                                 | 223 ms: 1.46x faster                                                   |
| scimark_sor             | 126 ms                                                 | 86.5 ms: 1.46x faster                                                  |
| nbody                   | 93.3 ms                                                | 64.1 ms: 1.46x faster                                                  |
| pickle_pure_python      | 283 us                                                 | 195 us: 1.46x faster                                                   |
| chaos                   | 66.7 ms                                                | 46.6 ms: 1.43x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 143 us: 1.43x faster                                                   |
| mako                    | 10.5 ms                                                | 7.36 ms: 1.42x faster                                                  |
| async_tree_none         | 400 ms                                                 | 286 ms: 1.40x faster                                                   |
| float                   | 72.4 ms                                                | 52.4 ms: 1.38x faster                                                  |
| pyflate                 | 453 ms                                                 | 328 ms: 1.38x faster                                                   |
| scimark_monte_carlo     | 72.5 ms                                                | 52.7 ms: 1.37x faster                                                  |
| pycparser               | 916 ms                                                 | 669 ms: 1.37x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 745 ms: 1.37x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.15 ms: 1.37x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 25.5 us: 1.35x faster                                                  |
| regex_compile           | 96.4 ms                                                | 73.0 ms: 1.32x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 28.3 ms: 1.31x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.44 ms: 1.31x faster                                                  |
| tornado_http            | 91.5 ms                                                | 70.3 ms: 1.30x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.05 ms: 1.30x faster                                                  |
| pprint_safe_repr        | 606 ms                                                 | 468 ms: 1.30x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 954 ms: 1.29x faster                                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.22 ms: 1.29x faster                                                  |
| genshi_text             | 18.4 ms                                                | 14.3 ms: 1.28x faster                                                  |
| generators              | 32.7 ms                                                | 25.5 ms: 1.28x faster                                                  |
| django_template         | 27.3 ms                                                | 21.3 ms: 1.28x faster                                                  |
| deepcopy                | 281 us                                                 | 221 us: 1.27x faster                                                   |
| spectral_norm           | 95.8 ms                                                | 75.2 ms: 1.27x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.64 us: 1.27x faster                                                  |
| logging_format          | 4.97 us                                                | 3.91 us: 1.27x faster                                                  |
| thrift                  | 580 us                                                 | 461 us: 1.26x faster                                                   |
| dulwich_log             | 37.1 ms                                                | 29.5 ms: 1.26x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 703 us: 1.25x faster                                                   |
| 2to3                    | 201 ms                                                 | 162 ms: 1.24x faster                                                   |
| xml_etree_process       | 44.8 ms                                                | 36.0 ms: 1.24x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.91 us: 1.24x faster                                                  |
| fannkuch                | 317 ms                                                 | 257 ms: 1.24x faster                                                   |
| html5lib                | 44.2 ms                                                | 35.8 ms: 1.24x faster                                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 542 ms: 1.24x faster                                                   |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.23 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.82 ms: 1.23x faster                                                  |
| docutils                | 1.78 sec                                               | 1.49 sec: 1.19x faster                                                 |
| sqlglot_optimize        | 38.0 ms                                                | 31.9 ms: 1.19x faster                                                  |
| scimark_fft             | 230 ms                                                 | 194 ms: 1.19x faster                                                   |
| mypy2                   | 307 ms                                                 | 261 ms: 1.17x faster                                                   |
| sqlalchemy_declarative  | 74.9 ms                                                | 63.9 ms: 1.17x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 466 us: 1.17x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.3 ms: 1.17x faster                                                  |
| comprehensions          | 17.6 us                                                | 15.1 us: 1.17x faster                                                  |
| sympy_str               | 169 ms                                                 | 147 ms: 1.15x faster                                                   |
| unpack_sequence         | 37.4 ns                                                | 32.7 ns: 1.14x faster                                                  |
| sympy_expand            | 275 ms                                                 | 243 ms: 1.13x faster                                                   |
| coroutines              | 20.2 ms                                                | 17.8 ms: 1.13x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 174 ms: 1.13x faster                                                   |
| sympy_sum               | 93.6 ms                                                | 83.8 ms: 1.12x faster                                                  |
| nqueens                 | 68.2 ms                                                | 61.1 ms: 1.12x faster                                                  |
| regex_v8                | 17.6 ms                                                | 15.8 ms: 1.11x faster                                                  |
| json                    | 3.08 ms                                                | 2.77 ms: 1.11x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.35 us: 1.10x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 97.6 ms: 1.09x faster                                                  |
| regex_dna               | 162 ms                                                 | 149 ms: 1.08x faster                                                   |
| mdp                     | 1.66 sec                                               | 1.54 sec: 1.08x faster                                                 |
| xml_etree_generate      | 54.2 ms                                                | 50.3 ms: 1.08x faster                                                  |
| pathlib                 | 28.8 ms                                                | 27.0 ms: 1.06x faster                                                  |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                                  |
| unpickle_list           | 2.69 us                                                | 2.57 us: 1.05x faster                                                  |
| telco                   | 3.63 ms                                                | 3.48 ms: 1.04x faster                                                  |
| unpickle                | 9.89 us                                                | 9.65 us: 1.02x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 76.3 ms: 1.02x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 70.9 ms: 1.02x faster                                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                                   |
| pickle_dict             | 17.9 us                                                | 18.1 us: 1.01x slower                                                  |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                                  |
| pickle_list             | 2.80 us                                                | 2.84 us: 1.01x slower                                                  |
| pickle                  | 7.35 us                                                | 7.56 us: 1.03x slower                                                  |
| python_startup          | 11.9 ms                                                | 12.4 ms: 1.04x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                  |
| async_generators        | 234 ms                                                 | 264 ms: 1.13x slower                                                   |
| bench_mp_pool           | 39.7 ms                                                | 46.2 ms: 1.16x slower                                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.4 ms: 1.17x slower                                                  |
| dask                    | 265 ms                                                 | 321 ms: 1.21x slower                                                   |
| coverage                | 42.0 ms                                                | 60.9 ms: 1.45x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                           |
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint
